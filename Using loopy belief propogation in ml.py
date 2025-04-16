import numpy as np
import itertools

def sample_partition(p01, p12):
    return (np.random.rand() < p01, np.random.rand() < p12)

def estimate_weights(p_cut):
    w01 = -np.log(p_cut[(0, 1)])
    w12 = -np.log(p_cut[(1, 2)])
    return w01, w12

def compute_Z_exact(w01, w12):
    total = 0
    for x0, x1, x2 in itertools.product([0,1], repeat=3):
        psi01 = np.exp(-w01 * (x0 != x1))
        psi12 = np.exp(-w12 * (x1 != x2))
        total += psi01 * psi12
    return total

true_Z = 4.0

print("Num Samples   | P(cut 0,1)  | P(cut 1,2)  | Est. w(0,1)  | Est. w(1,2)  | Est. Z     | Rel. Error")
print("-----------------------------------------------------------------------------------------------")

for num_samples in [10, 100, 1000, 10000, 100000]:
    cuts = {(0, 1): 0, (1, 2): 0}
    for _ in range(num_samples):
        s01, s12 = sample_partition(0.1, 0.9)
        if s01:
            cuts[(0, 1)] += 1
        if s12:
            cuts[(1, 2)] += 1
    p_cut = {
        (0, 1): cuts[(0, 1)] / num_samples if cuts[(0,1)] > 0 else 1e-10,
        (1, 2): cuts[(1, 2)] / num_samples if cuts[(1,2)] > 0 else 1e-10
    }
    w01, w12 = estimate_weights(p_cut)
    Z_est = compute_Z_exact(w01, w12)
    rel_error = abs(Z_est - true_Z) / true_Z
    print(f"{num_samples:<14}| {p_cut[(0,1)]:<11.6f} | {p_cut[(1,2)]:<11.6f} | {w01:<12.6f} | {w12:<12.6f} | {Z_est:<10.6f} | {rel_error:<10.6f}")
