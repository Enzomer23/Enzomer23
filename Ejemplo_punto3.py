import numpy as np

patterns = np.array([[1, 1, 1, -1],
                     [1, -1, -1, -1],
                     [1, 1, 1, -1]])

incomplete_pattern = np.array([1, 1, -1, 1])

weights = np.zeros((patterns.shape[1], patterns.shape[1]))
for pattern in patterns:
    weights += np.outer(pattern, pattern)

recovered_pattern = np.sign(np.dot(weights, incomplete_pattern))

print("Patron recuperado:", recovered_pattern)
