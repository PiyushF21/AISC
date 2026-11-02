# import numpy as np
# # Given input data
# X = np.array([
#     [0.2, 0.4],
#     [0.5, 0.6],
#     [0.8, 0.9]
# ])
# # Given initial weights (2x2 grid, 2 features)
# weights = np.array([
#     [[0.1, 0.2], [0.3, 0.4]],
#     [[0.5, 0.6], [0.7, 0.8]]
# ])

# rows = 2
# cols = 2
# learning_rate = 0.5
# epochs = 10
# radius = 1
# # SOM Training
# for epoch in range(epochs):
#     for sample in X:
#         # Find distances
#         distances = np.linalg.norm(weights - sample, axis=2)
#         # Find BMU
#         bmu = np.unravel_index(np.argmin(distances), distances.shape)
#         # Update weights
#         for i in range(rows):
#             for j in range(cols):
#                 d = np.sqrt((i-bmu[0])**2 + (j-bmu[1])**2)
#                 if d <= radius:
#                     weights[i,j] += learning_rate * (sample - weights[i,j])
# # Testing
# for sample in X:
#     distances = np.linalg.norm(weights - sample, axis=2)
#     bmu = np.unravel_index(np.argmin(distances), distances.shape)
#     print("Input:", sample, "BMU:", bmu)
# print("Final Weights:")
# print(weights)

# import numpy as np

# X = np.array([
#     [0.3, 0.5],
#     [0.6, 0.7],
#     [0.8, 0.2]
# ])

# W = np.array([
#     [0.2, 0.4],
#     [0.5, 0.6],
#     [0.1, 0.8],
#     [0.7, 0.3],
#     [0.9, 0.5]
# ])

# learning_rate = 0.5
# epochs = 10

# for epoch in range(epochs):
#     for sample in X:
#         # Calculate Euclidean distance
#         distances = np.linalg.norm(W - sample, axis=1)
#         # Find winning neuron
#         bmu = np.argmin(distances)
#         # Update winning neuron's weights
#         W[bmu] += learning_rate * (sample - W[bmu])

# print("Final Weights:")
# print(W)

# # Testing
# for sample in X:
#     distances = np.linalg.norm(W - sample, axis=1)
#     bmu = np.argmin(distances)
#     print("Input:", sample, "Winning Neuron:", bmu)


import numpy as np
x = np.array([[0.2,0.4]])
w=np.array([[0.3,0.5],[0.2,0.6],[0.1,0.7],[0.8,0.9],[0.4,0.2]])

epochs = 1000
learning_rate = 0.2

for i in range(epochs):
    for sample in x:
        distances = np.linalg.norm(w-sample,axis=1)
        bmu = np.argmin(distances)
        w[bmu]+=learning_rate*(sample-w[bmu])

import numpy as np

W = np.array([
    [0.3, 0.5],
    [0.2, 0.6],
    [0.1, 0.7],
    [0.8, 0.9],
    [0.4, 0.2]
])

def SOM(X, lr):
    global W

    # Calculate squared Euclidean distance
    distances = np.sum((W - X)**2, axis=1)

    # Find winning neuron
    Y = np.argmin(distances)

    print("Distances:", distances)
    print("Winning neuron:", Y + 1)

    # Update winning neuron's weights
    W[Y] = W[Y] + lr * (X - W[Y])

    print("New weights:", W[Y])


# Part (a)
SOM(np.array([0.2, 0.4]), 0.2)

# Part (b)
SOM(np.array([0.6, 0.6]), 0.1)