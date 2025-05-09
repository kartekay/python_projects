import numpy as np
import pandas as pd
from itertools import permutations
from sklearn.model_selection import train_test_split

# ================================
# TASK 1: EM for Graph Edge Weights (Latent + k-ary Support)
# ================================

def setup_graph(adjacency_matrix):
    edge_array = np.transpose(np.nonzero(np.triu(adjacency_matrix)))
    edge_to_index = {tuple(edge): idx for idx, edge in enumerate(edge_array)}
    return edge_array, edge_to_index

def setup_neighbors_and_msgs(node_count, edge_array, k):
    adj_list = [[] for _ in range(node_count)]
    for u, v in edge_array:
        adj_list[u].append(v)
        adj_list[v].append(u)
    bp_msgs = {(u, v): np.ones(k) / k for u, v in edge_array}
    bp_msgs.update({(v, u): np.ones(k) / k for u, v in edge_array})
    return adj_list, bp_msgs

def capped_exp(x):
    return np.clip(np.exp(x), 0, 1e10)

def create_compatibility_matrix(wt, k):
    mat = np.ones((k, k))
    for i in range(k):
        for j in range(k):
            if i != j:
                mat[i, j] = capped_exp(wt)
    return mat

def run_belief_propagation(node_count, edge_array, edge_to_index, edge_weights, observed_labels, k=2, max_iter=10, tolerance=1e-3):
    adj_list, bp_msgs = setup_neighbors_and_msgs(node_count, edge_array, k)
    for _ in range(max_iter):
        previous_msgs = bp_msgs.copy()
        for u in range(node_count):
            if observed_labels[u] != -1:
                continue
            for v in adj_list[u]:
                msg_product = np.ones(k)
                for neighbor in adj_list[u]:
                    if neighbor != v:
                        msg_product *= bp_msgs[(neighbor, u)]
                edge_idx = edge_to_index.get((u, v), edge_to_index.get((v, u)))
                compatibility = create_compatibility_matrix(edge_weights[edge_idx], k)
                new_msg = compatibility.T @ msg_product
                new_msg /= np.sum(new_msg)
                bp_msgs[(u, v)] = new_msg
        delta_change = sum(np.linalg.norm(bp_msgs[k] - previous_msgs[k]) for k in bp_msgs)
        if delta_change < tolerance:
            break
    return compute_edge_probs(edge_array, edge_weights, bp_msgs, observed_labels, k)

def compute_edge_probs(edge_array, edge_weights, bp_msgs, observed_labels, k):
    marginals = np.zeros(len(edge_array))
    for idx, (u, v) in enumerate(edge_array):
        if observed_labels[u] != -1 and observed_labels[v] != -1:
            marginals[idx] = 1.0 if observed_labels[u] != observed_labels[v] else 0.0
            continue
        mu_u, mu_v = bp_msgs[(u, v)], bp_msgs[(v, u)]
        compatibility = create_compatibility_matrix(edge_weights[idx], k)
        joint_dist = np.outer(mu_u, mu_v) * compatibility
        joint_dist /= np.sum(joint_dist)
        marginals[idx] = 1.0 - np.trace(joint_dist)
    return marginals

def estimate_logZ_gradient(edge_weights, edge_array, edge_to_index, node_count, k=2, trials=5):
    sum_marginals = np.zeros(len(edge_array))
    for _ in range(trials):
        unknowns = np.full(node_count, -1)
        edge_estimates = run_belief_propagation(node_count, edge_array, edge_to_index, edge_weights, unknowns, k)
        sum_marginals += edge_estimates
    return sum_marginals / trials

def bound_gradients(gradient, cap=1.0):
    return np.clip(gradient, -cap, cap)

def compute_log_likelihood(edge_weights, edge_array, edge_to_index, node_count, sample_matrix, L, k):
    total_log_likelihood = 0.0
    num_samples = sample_matrix.shape[1]
    for sample_idx in range(num_samples):
        sample = sample_matrix[:, sample_idx]
        labels = np.full(node_count, -1)
        labels[L == 0] = sample[L == 0]
        log_prob = 0.0
        for idx, (u, v) in enumerate(edge_array):
            wt = edge_weights[idx]
            if labels[u] == -1 or labels[v] == -1:
                continue
            prob = 1.0 if labels[u] == labels[v] else capped_exp(wt)
            log_prob += np.log(prob + 1e-10)
        total_log_likelihood += log_prob
    return total_log_likelihood / num_samples

def execute_cut_em(A, L, samples, max_epochs=20, tolerance=1e-3, lr=0.01, min_epochs=5):
    num_nodes, num_samples = samples.shape
    edge_array, edge_to_index = setup_graph(A)
    edge_weights = np.random.randn(len(edge_array)) * 0.01
    k = int(np.max(samples) + 1)
    for epoch in range(max_epochs):
        accum_expected = np.zeros(len(edge_array))
        for sample_idx in range(num_samples):
            sample = samples[:, sample_idx]
            observed = np.full(num_nodes, -1)
            observed[L == 0] = sample[L == 0]
            edge_probs = run_belief_propagation(num_nodes, edge_array, edge_to_index, edge_weights, observed, k)
            accum_expected += edge_probs
        accum_expected /= num_samples
        gradient = accum_expected - estimate_logZ_gradient(edge_weights, edge_array, edge_to_index, num_nodes, k)
        gradient = bound_gradients(gradient)
        edge_weights += lr * gradient

        log_likelihood = compute_log_likelihood(edge_weights, edge_array, edge_to_index, num_nodes, samples, L, k)
        print(f"Epoch {epoch+1}: Mean weight = {np.mean(edge_weights):.4f}, Max grad = {np.max(np.abs(gradient)):.4f}, Log-Likelihood = {log_likelihood:.4f}")
        if np.linalg.norm(gradient) < tolerance and epoch >= min_epochs:
            break
    return edge_weights

# ================================
# DEMO Task 1: Cut EM
# ================================

def demo_cutsem():
    A = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    L = np.array([1, 0, 1])  # 1 = latent, 0 = observed
    samples = np.array([[0, 1, 1], [1, 1, 0], [0, 0, 1]])
    weights = execute_cut_em(A, L, samples, max_epochs=20)
    print(f"Final weights: {weights}")
    return weights

# ================================
# TASK 2: Improved EM for Discrete Bayes Net
# ================================

def laplace_cpd(df, parent_col, child_col):
    if parent_col:
        cross_tab = pd.crosstab(df[parent_col], df[child_col])
        smoothed = (cross_tab + 1).div((cross_tab + 1).sum(axis=1), axis=0)
    else:
        counts = df[child_col].value_counts()
        smoothed = (counts + 1) / (counts.sum() + len(counts))
    return smoothed

def setup_initial_cpds(df, bn_structure):
    cpds_dict = {}
    for parent, child in bn_structure:
        cpds_dict[(parent, child)] = laplace_cpd(df, parent, child)
    return cpds_dict

def perform_em_update(df, current_cpds, bn_structure):
    updated_df = df.copy()
    for col in df.columns:
        if df[col].isnull().any():
            updated_df[col] = df[col].fillna(df[col].mode()[0])
    return setup_initial_cpds(updated_df, bn_structure)

def learn_cpds_em(df, bn_structure, max_loops=100, tolerance=1e-4):
    cpds = setup_initial_cpds(df, bn_structure)
    for _ in range(max_loops):
        new_cpds = perform_em_update(df, cpds, bn_structure)
        if all(np.allclose(cpds[k].values, new_cpds[k].values, atol=tolerance) for k in cpds if hasattr(cpds[k], 'values')):
            break
        cpds = new_cpds
    return cpds

def classify_instances(df, cpds, bn_structure):
    results = []
    for _, instance in df.iterrows():
        probs = pd.Series({label: 1.0 for label in ['democrat', 'republican']})
        for parent, child in bn_structure:
            if child == 'party':
                if instance[parent] in cpds[(parent, child)].index:
                    probs *= cpds[(parent, child)].loc[instance[parent]]
            else:
                if instance[parent] in cpds[(parent, child)].index:
                    conditional = cpds[(parent, child)].loc[instance[parent]]
                    probs = probs.multiply(conditional, fill_value=1)
        results.append(probs.idxmax())
    return results

# ================================
# DEMO Task 2: Bayes Net EM
# ================================

def demo_bayes_net_em():
    df_votes = pd.read_csv('house-votes-84.data', names=['party'] + [f'vote{i}' for i in range(1, 17)])
    df_votes.replace({'?': np.nan, 'n': 0, 'y': 1}, inplace=True)
    df_votes = df_votes[['party', 'vote1', 'vote2']][:300]
    train_df, test_df = train_test_split(df_votes, test_size=0.3, random_state=42)
    model_scores = {}
    all_bn_structures = [perm for perm in permutations(['party', 'vote1', 'vote2'], 3)]
    for bn_perm in all_bn_structures:
        bn_edges = [(bn_perm[0], bn_perm[1]), (bn_perm[1], bn_perm[2])]
        cpds = learn_cpds_em(train_df, bn_edges)
        pred_labels = classify_instances(test_df, cpds, bn_edges)
        acc = (pred_labels == test_df['party']).mean()
        model_scores[bn_perm] = acc
        print(f"Structure_Votes: {bn_perm}, Acc.: {acc:.4f}")

# ================================
# DEMO BOTH TASKS
# ================================

if __name__ == "__main__":
    print("Running Task 1: Graph Edge Weight EM...")
    demo_cutsem()
    print("\nRunning Task 2: Bayes Net EM...")
    demo_bayes_net_em()
