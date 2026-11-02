# import numpy as np

# # Training data
# X = np.array([
#     [0, 0, 1, 1],
#     [1, 0, 0, 0],
#     [0, 0, 0, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 0]
# ])

# # Actual classes
# Y = np.array([1, 2, 2, 1, 1])

# # Initial weights: one prototype for each class
# W = np.array([
#     X[0],       # Class 1
#     X[1]        # Class 2
# ])

# C = np.array([1, 2])

# lr = 0.1
# epochs = 10

# # Training
# for epoch in range(epochs):
#     for i in range(len(X)):

#         distances = np.linalg.norm(W - X[i], axis=1)

#         winner = np.argmin(distances)

#         if C[winner] == Y[i]:
#             W[winner] = W[winner] + lr * (X[i] - W[winner])
#         else:
#             W[winner] = W[winner] - lr * (X[i] - W[winner])

# # Testing
# for sample in X:
#     distances = np.linalg.norm(W - sample, axis=1)
#     winner = np.argmin(distances)

#     print("Input:", sample, "Predicted Class:", C[winner])

# print("Final Weights:")
# print(W)

import numpy as np
X = np.array([
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0]
])

# Actual classes
Y = np.array([1, 2, 2, 1, 1])

W = np.array([X[0],X[1]])
learning_rate = 0.2
epochs = 1000
C=np.array([1,2])
for epoch in range(epochs):
    for i in range(len(X)):
        distances = np.linalg.norm(W-X[i],axis=1)
        winner = np.argmin(distances)
        if C[winner]==Y[i]:
            W[winner]+=learning_rate*(X[i]-W[winner])
        else:
            W[winner]-=learning_rate*(X[i]-W[winner])

