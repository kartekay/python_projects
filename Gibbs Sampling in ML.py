import numpy as np
from numba import njit

@njit
def gibbs(A, s, t, w, burnin, its):
    n = A.shape[0]
    state = np.random.randint(0, 2, size=n)
    state[s] = 1
    state[t] = 0
    samples = np.zeros(n)

    for i in range(burnin + its):
        for node in range(n):
            if node == s or node == t:
                continue
            score_0, score_1 = 0.0, 0.0
            for nbr in range(n):
                if A[node, nbr] != 0:
                    weight = w[node, nbr]
                    score_0 += weight * (state[nbr] != 0)
                    score_1 += weight * (state[nbr] != 1)
            p1 = np.exp(-score_1)
            p0 = np.exp(-score_0)
            prob = p1 / (p1 + p0)
            state[node] = 1 if np.random.rand() < prob else 0
        if i >= burnin:
            samples += state
    return samples / its


node_indices = {'s': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 't': 7}
n = 8
A = np.zeros((n, n))
edges = [('s', 'a'), ('s', 'b'), ('a', 'd'), ('a', 'c'), ('b', 'c'), ('c', 'e'),
         ('d', 'e'), ('d', 'f'), ('e', 'f'), ('e', 't'), ('f', 't')]
for u, v in edges:
    i, j = node_indices[u], node_indices[v]
    A[i, j] = A[j, i] = 1

w = A * 0.5


burnin_values = [2**6, 2**10, 2**14]
its_values = [2**10, 2**14, 2**18]
results = {}


for burnin in burnin_values:
    for its in its_values:
        marginals = gibbs(A, s=node_indices['s'], t=node_indices['t'], w=w,
                          burnin=burnin, its=its)
        results[(burnin, its)] = marginals[node_indices['e']]


print(f"{'Burn-in':>10} {'Iterations':>12} {'Marginal of e':>15}")
print("=" * 40)
for (burnin, its), val in results.items():
    print(f"{burnin:>10} {its:>12} {val:>15.5f}")
