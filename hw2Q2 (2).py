import numpy as np


def sumprod_maxprod(M, s, t, w, its):
    n = M.shape[0]

    messages_sum = np.ones((n, n, 2))
    messages_max = np.ones((n, n, 2))

    for _ in range(its):
        new_messages_sum = np.ones_like(messages_sum)
        new_messages_max = np.ones_like(messages_max)

        for i in range(n):
            for j in range(n):
                if M[i, j]:
                    msg_sum = np.zeros(2)
                    msg_max = np.zeros(2)

                    for k in range(n):
                        if k != j and M[k, i]:
                            msg_sum[0] += messages_sum[k, i, 0]
                            msg_sum[1] += messages_sum[k, i, 1]
                            msg_max[0] = max(msg_max[0], messages_max[k, i, 0])
                            msg_max[1] = max(msg_max[1], messages_max[k, i, 1])

                    new_messages_sum[i, j, 0] = w[i, j] * (msg_sum[0] + msg_sum[1])
                    new_messages_sum[i, j, 1] = w[i, j] * (msg_sum[0] + msg_sum[1])
                    new_messages_max[i, j, 0] = max(w[i, j] + msg_max[1], msg_max[0])
                    new_messages_max[i, j, 1] = max(msg_max[0], w[i, j] + msg_max[1])

        messages_sum = new_messages_sum
        messages_max = new_messages_max

    beliefs_sum = np.ones((n, 2))
    beliefs_max = np.ones((n, 2))
    for i in range(n):
        for j in range(n):
            if M[i, j]:
                beliefs_sum[i] *= messages_sum[j, i]
                beliefs_max[i] *= messages_max[j, i]
        beliefs_sum[i] /= np.sum(beliefs_sum[i]) + 1e-10
        beliefs_max[i] /= np.sum(beliefs_max[i]) + 1e-10

    beliefs_max[s] = [1, 0]
    beliefs_max[t] = [0, 1]

    x = np.zeros(n)
    x[s] = 1
    x[t] = 0

    for i in range(n):
        if np.argmax(beliefs_max[i]) == 0:
            x[i] = 0
        else:
            x[i] = 1

    for i in range(n):
        if np.isclose(beliefs_max[i, 0], beliefs_max[i, 1]):
            x[i] = 0.5

    Z = np.sum(beliefs_sum[:, 0] + beliefs_sum[:, 1])

    return Z, x


M = np.array([[0, 1, 1, 0],
              [1, 0, 1, 1],
              [1, 1, 0, 1],
              [0, 1, 1, 0]])

w = np.array([[0, 0.5, 0.8, 0],
              [0.5, 0, 0.6, 0.7],
              [0.8, 0.6, 0, 0.9],
              [0, 0.7, 0.9, 0]])

s, t, its = 0, 3, 10
Z, x = sumprod_maxprod(M, s, t, w, its)

print("Approximate Partition Function:", Z)
print("Approximate Max Cut Assignment:", x)

if np.any(x == 0.5):
    print("Max cut assignment is not unique.")
else:
    print("Max cut assignment is unique.")
