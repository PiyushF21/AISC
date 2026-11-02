# alpha = float(input("Enter learning rate (alpha): "))

# n = int(input("Enter number of inputs/features: "))

# samples = int(input("Enter number of training samples: "))

# epochs = int(input("Enter number of epochs: "))


# weights = []

# print("\nEnter initial weights:")

# for i in range(n):
#     w = float(input(f"W{i+1}: "))
#     weights.append(w)

# bias = float(input("Enter initial bias B: "))


# X = []
# T = []

# print("\nEnter training data:")

# for i in range(samples):

#     print(f"\nSample {i+1}")

#     inputs = []

#     for j in range(n):
#         value = float(input(f"X{j+1}: "))
#         inputs.append(value)

#     target = float(input("Target (t): "))

#     X.append(inputs)
#     T.append(target)


# def activation(yin):

#     if yin == 0:
#         return 0
#     elif yin < 0:
#         return -1
#     else:
#         return 1


# for epoch in range(1, epochs + 1):

#     print(f"EPOCH {epoch}")
#     print("=" * 70)

#     print("X", end="\t")
#     print("t\tY", end="\t")

#     for i in range(n):
#         print(f"W{i+1}", end="\t")

#     print("B")

#     for i in range(samples):

#         inputs = X[i]

#         t = T[i]

#         yin = bias

#         for j in range(n):
#             yin += weights[j] * inputs[j]

#         y = activation(yin)

#         if t != y:

#             for j in range(n):
#                 delta_w = alpha * t * inputs[j]
#                 weights[j] = weights[j] + delta_w

#             delta_b = alpha * t
#             bias = bias + delta_b

#         print("(", end="")

#         for j in range(n):
#             print(inputs[j], end="")

#             if j != n - 1:
#                 print(",", end="")

#         print(")", end="\t")

#         print(f"{t}\t{y}", end="\t")

#         for w in weights:
#             print(w, end="\t")

#         print(bias)

#     print("\nEnd of Epoch", epoch)
#     print("Weights:", weights)
#     print("Bias:", bias)


# Single Layer Perceptron

# Training data for AND gate
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

Y = [0, 0, 0, 1]

# Initialize weights and bias
weights = [0, 0]
bias = 0

learning_rate = 0.1
epochs = 10


# Activation function
def activation(value):
    return 1 if value >= 0 else 0
# Training
for epoch in range(epochs):

    for i in range(len(X)):

        inputs = X[i]
        target = Y[i]

        # Calculate weighted sum
        total = sum(inputs[j] * weights[j]
                    for j in range(len(weights))) + bias

        # Predict output
        prediction = activation(total)

        # Calculate error
        error = target - prediction

        # Update weights and bias
        for j in range(len(weights)):
            weights[j] += learning_rate * error * inputs[j]

        bias += learning_rate * error


# Testing
print("A B | Output")

for inputs in X:

    total = sum(inputs[j] * weights[j]
                for j in range(len(weights))) + bias

    output = activation(total)

    print(inputs[0], inputs[1], "|", output)

print("Final Weights:", weights)
print("Final Bias:", bias)

