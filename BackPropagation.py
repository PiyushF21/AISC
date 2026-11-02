# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# np.random.seed(42)

# # ============================================================
# # 1. CREATE SYNTHETIC DATASET
# # ============================================================

# n_samples = 600

# income = np.random.randint(20000, 150001, n_samples)
# age = np.random.randint(21, 61, n_samples)
# credit_score = np.random.randint(500, 851, n_samples)

# # Normalize input features
# income_n = (income - 20000) / (150000 - 20000)
# age_n = (age - 21) / (60 - 21)
# credit_n = (credit_score - 500) / (850 - 500)

# # Generate synthetic loan eligibility score
# score = (
#     0.55 * credit_n +
#     0.35 * income_n +
#     0.10 * age_n +
#     np.random.normal(0, 0.03, n_samples)
# )

# # Create binary target
# threshold = np.median(score)
# approved = (score >= threshold).astype(int)

# df = pd.DataFrame({
#     "Income": income,
#     "Age": age,
#     "CreditScore": credit_score,
#     "LoanApproved": approved
# })

# print("Dataset Shape:", df.shape)
# print("\nFirst 10 records:")
# print(df.head(10))

# print("\nClass Distribution:")
# print(df["LoanApproved"].value_counts().sort_index())


# # ============================================================
# # 2. PREPARE INPUT AND OUTPUT
# # ============================================================

# X = np.column_stack([
#     income_n,
#     age_n,
#     credit_n
# ])

# y = approved.reshape(-1, 1).astype(float)


# # ============================================================
# # 3. 80% TRAINING AND 20% TESTING
# # ============================================================

# train_indices = []
# test_indices = []

# for cls in [0, 1]:

#     indices = np.where(approved == cls)[0]

#     np.random.shuffle(indices)

#     split = int(0.80 * len(indices))

#     train_indices.extend(indices[:split])
#     test_indices.extend(indices[split:])

# train_indices = np.array(train_indices)
# test_indices = np.array(test_indices)

# np.random.shuffle(train_indices)
# np.random.shuffle(test_indices)

# X_train = X[train_indices]
# y_train = y[train_indices]

# X_test = X[test_indices]
# y_test = y[test_indices]

# print("\nTraining Samples:", len(X_train))
# print("Testing Samples:", len(X_test))


# # ============================================================
# # 4. CUSTOM NEURAL NETWORK
# # Architecture: 3 -> 8 -> 1
# # ============================================================

# class CustomNeuralNetwork:

#     def __init__(
#         self,
#         input_size=3,
#         hidden_size=8,
#         learning_rate=0.1,
#         seed=7
#     ):

#         rng = np.random.default_rng(seed)

#         self.learning_rate = learning_rate

#         # Input -> Hidden weights
#         self.W1 = rng.normal(
#             0,
#             0.25,
#             (input_size, hidden_size)
#         )

#         # Hidden biases
#         self.b1 = np.zeros(
#             (1, hidden_size)
#         )

#         # Hidden -> Output weights
#         self.W2 = rng.normal(
#             0,
#             0.25,
#             (hidden_size, 1)
#         )

#         # Output bias
#         self.b2 = np.zeros(
#             (1, 1)
#         )


#     # ========================================================
#     # Sigmoid
#     # ========================================================

#     @staticmethod
#     def sigmoid(z):

#         z = np.clip(z, -500, 500)

#         return 1 / (1 + np.exp(-z))


#     # ========================================================
#     # Forward Propagation
#     # ========================================================

#     def forward(self, X):

#         # Hidden layer
#         self.z1 = X @ self.W1 + self.b1

#         self.a1 = self.sigmoid(
#             self.z1
#         )

#         # Output layer
#         self.z2 = self.a1 @ self.W2 + self.b2

#         self.a2 = self.sigmoid(
#             self.z2
#         )

#         return self.a2


#     # ========================================================
#     # Training using Backpropagation
#     # ========================================================

#     def train(
#         self,
#         X,
#         y,
#         epochs=5000,
#         verbose_every=500
#     ):

#         n = X.shape[0]

#         history = {
#             "epoch": [],
#             "mse": [],
#             "accuracy": [],
#             "precision": [],
#             "recall": [],
#             "f1": []
#         }

#         for epoch in range(1, epochs + 1):

#             # Forward propagation
#             y_pred = self.forward(X)

#             # Error
#             error = y - y_pred

#             mse = np.mean(
#                 error ** 2
#             )

#             # Backpropagation

#             # Output layer delta
#             delta2 = (
#                 error
#                 * y_pred
#                 * (1 - y_pred)
#             )

#             # Hidden layer delta
#             delta1 = (
#                 (delta2 @ self.W2.T)
#                 * self.a1
#                 * (1 - self.a1)
#             )

#             # Gradients

#             dW2 = (
#                 self.a1.T @ delta2
#             ) / n

#             db2 = np.mean(
#                 delta2,
#                 axis=0,
#                 keepdims=True
#             )

#             dW1 = (
#                 X.T @ delta1
#             ) / n

#             db1 = np.mean(
#                 delta1,
#                 axis=0,
#                 keepdims=True
#             )

#             # Weight and bias update

#             self.W2 += (
#                 self.learning_rate * dW2
#             )

#             self.b2 += (
#                 self.learning_rate * db2
#             )

#             self.W1 += (
#                 self.learning_rate * dW1
#             )

#             self.b1 += (
#                 self.learning_rate * db1
#             )

#             # Training metrics

#             predictions = (
#                 y_pred >= 0.5
#             ).astype(int)

#             tp = np.sum(
#                 (predictions == 1)
#                 & (y == 1)
#             )

#             tn = np.sum(
#                 (predictions == 0)
#                 & (y == 0)
#             )

#             fp = np.sum(
#                 (predictions == 1)
#                 & (y == 0)
#             )

#             fn = np.sum(
#                 (predictions == 0)
#                 & (y == 1)
#             )

#             accuracy = (
#                 (tp + tn) / n
#             )

#             precision = (
#                 tp / (tp + fp)
#                 if tp + fp
#                 else 0
#             )

#             recall = (
#                 tp / (tp + fn)
#                 if tp + fn
#                 else 0
#             )

#             f1 = (
#                 2 * precision * recall
#                 / (precision + recall)
#                 if precision + recall
#                 else 0
#             )

#             history["epoch"].append(epoch)
#             history["mse"].append(mse)
#             history["accuracy"].append(accuracy)
#             history["precision"].append(precision)
#             history["recall"].append(recall)
#             history["f1"].append(f1)

#             if (
#                 epoch == 1
#                 or epoch % verbose_every == 0
#             ):

#                 print(
#                     f"Epoch {epoch:4d} | "
#                     f"MSE: {mse:.6f} | "
#                     f"Accuracy: {accuracy * 100:.2f}% | "
#                     f"Precision: {precision:.4f} | "
#                     f"Recall: {recall:.4f} | "
#                     f"F1: {f1:.4f}"
#                 )

#         return pd.DataFrame(history)


#     # ========================================================
#     # Prediction Probability
#     # ========================================================

#     def predict_proba(self, X):

#         return self.forward(X)


#     # ========================================================
#     # Final Prediction
#     # ========================================================

#     def predict(self, X):

#         return (
#             self.predict_proba(X) >= 0.5
#         ).astype(int)


# # ============================================================
# # 5. CREATE AND TRAIN MODEL
# # ============================================================

# model = CustomNeuralNetwork(
#     input_size=3,
#     hidden_size=8,
#     learning_rate=0.1,
#     seed=7
# )

# history = model.train(
#     X_train,
#     y_train,
#     epochs=5000,
#     verbose_every=500
# )


# # ============================================================
# # 6. EPOCH-WISE TRAINING TABLE
# # ============================================================

# epoch_table = history[
#     (history["epoch"] == 1) |
#     (history["epoch"] % 500 == 0)
# ].copy()

# epoch_table["Accuracy (%)"] = (
#     epoch_table["accuracy"] * 100
# )

# epoch_table["Precision (%)"] = (
#     epoch_table["precision"] * 100
# )

# epoch_table["Recall (%)"] = (
#     epoch_table["recall"] * 100
# )

# epoch_table["F1 (%)"] = (
#     epoch_table["f1"] * 100
# )

# epoch_table = epoch_table[
#     [
#         "epoch",
#         "mse",
#         "Accuracy (%)",
#         "Precision (%)",
#         "Recall (%)",
#         "F1 (%)"
#     ]
# ]

# epoch_table.columns = [
#     "Epoch",
#     "MSE",
#     "Accuracy (%)",
#     "Precision (%)",
#     "Recall (%)",
#     "F1 (%)"
# ]

# print("\nEpoch-wise Training Results:")
# print(epoch_table)


# # ============================================================
# # 7. TRAINING GRAPHS
# # ============================================================

# plt.figure(figsize=(9, 5))

# plt.plot(
#     history["epoch"],
#     history["mse"]
# )

# plt.xlabel("Epoch")
# plt.ylabel("MSE")
# plt.title("Mean Squared Error vs Epoch")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(9, 5))

# plt.plot(
#     history["epoch"],
#     history["accuracy"] * 100
# )

# plt.xlabel("Epoch")
# plt.ylabel("Accuracy (%)")
# plt.title("Training Accuracy vs Epoch")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(9, 5))

# plt.plot(
#     history["epoch"],
#     history["precision"] * 100
# )

# plt.xlabel("Epoch")
# plt.ylabel("Precision (%)")
# plt.title("Precision vs Epoch")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(9, 5))

# plt.plot(
#     history["epoch"],
#     history["recall"] * 100
# )

# plt.xlabel("Epoch")
# plt.ylabel("Recall (%)")
# plt.title("Recall vs Epoch")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(9, 5))

# plt.plot(
#     history["epoch"],
#     history["f1"] * 100
# )

# plt.xlabel("Epoch")
# plt.ylabel("F1 Score (%)")
# plt.title("F1 Score vs Epoch")
# plt.grid(True)
# plt.show()


# # ============================================================
# # 8. DETAILED FORWARD PROPAGATION
# # ============================================================

# sample_X = X_train[:1]
# sample_y = y_train[:1]

# z1 = (
#     sample_X @ model.W1
#     + model.b1
# )

# a1 = model.sigmoid(z1)

# z2 = (
#     a1 @ model.W2
#     + model.b2
# )

# y_hat = model.sigmoid(z2)

# error = (
#     sample_y - y_hat
# )

# delta2 = (
#     error
#     * y_hat
#     * (1 - y_hat)
# )

# delta1 = (
#     (delta2 @ model.W2.T)
#     * a1
#     * (1 - a1)
# )

# print("\nInput:")
# print(sample_X)

# print("\nTarget:")
# print(sample_y)

# print("\nZ1:")
# print(z1)

# print("\nA1:")
# print(a1)

# print("\nZ2:")
# print(z2)

# print("\nPredicted Output Y_hat:")
# print(y_hat)

# print("\nError:")
# print(error)

# print("\nDelta2:")
# print(delta2)

# print("\nDelta1:")
# print(delta1)


# # ============================================================
# # 9. FINAL WEIGHTS AND BIASES
# # ============================================================

# print("\nW1 - Input to Hidden Weights:")
# print(model.W1)

# print("\nB1 - Hidden Layer Bias:")
# print(model.b1)

# print("\nW2 - Hidden to Output Weights:")
# print(model.W2)

# print("\nB2 - Output Bias:")
# print(model.b2)


# # ============================================================
# # 10. TEST SET EVALUATION
# # ============================================================

# test_prob = model.predict_proba(X_test)

# test_pred = (
#     test_prob >= 0.5
# ).astype(int)


# tp = int(
#     np.sum(
#         (test_pred == 1)
#         & (y_test == 1)
#     )
# )

# tn = int(
#     np.sum(
#         (test_pred == 0)
#         & (y_test == 0)
#     )
# )

# fp = int(
#     np.sum(
#         (test_pred == 1)
#         & (y_test == 0)
#     )
# )

# fn = int(
#     np.sum(
#         (test_pred == 0)
#         & (y_test == 1)
#     )
# )


# accuracy = (
#     (tp + tn)
#     / len(y_test)
# )

# precision = (
#     tp / (tp + fp)
#     if tp + fp
#     else 0
# )

# recall = (
#     tp / (tp + fn)
#     if tp + fn
#     else 0
# )

# specificity = (
#     tn / (tn + fp)
#     if tn + fp
#     else 0
# )

# f1 = (
#     2 * precision * recall
#     / (precision + recall)
#     if precision + recall
#     else 0
# )

# mse = np.mean(
#     (y_test - test_prob) ** 2
# )


# # ============================================================
# # 11. FINAL METRICS TABLE
# # ============================================================

# metrics_table = pd.DataFrame({
#     "Metric": [
#         "MSE",
#         "Accuracy",
#         "Precision",
#         "Recall",
#         "Specificity",
#         "F1 Score"
#     ],

#     "Value": [
#         mse,
#         accuracy * 100,
#         precision * 100,
#         recall * 100,
#         specificity * 100,
#         f1 * 100
#     ]
# })

# print("\nFinal Test Metrics:")
# print(metrics_table)


# # ============================================================
# # 12. CONFUSION MATRIX
# # ============================================================

# cm = np.array([
#     [tn, fp],
#     [fn, tp]
# ])

# plt.figure(figsize=(7, 5))

# plt.imshow(
#     cm,
#     interpolation="nearest"
# )

# plt.title("Confusion Matrix")

# plt.colorbar()

# classes = [
#     "Not Approved (0)",
#     "Approved (1)"
# ]

# plt.xticks(
#     [0, 1],
#     classes
# )

# plt.yticks(
#     [0, 1],
#     classes
# )

# for i in range(2):
#     for j in range(2):

#         plt.text(
#             j,
#             i,
#             str(cm[i, j]),
#             ha="center",
#             va="center",
#             fontsize=16,
#             fontweight="bold"
#         )

# plt.xlabel("Predicted Label")
# plt.ylabel("Actual Label")

# plt.tight_layout()
# plt.show()


# # ============================================================
# # 13. ROC CURVE AND ROC-AUC
# # ============================================================

# y_true = y_test.flatten().astype(int)

# scores = test_prob.flatten()

# thresholds = np.r_[
#     np.inf,
#     np.sort(
#         np.unique(scores)
#     )[::-1]
# ]

# tpr_list = []
# fpr_list = []

# P = np.sum(
#     y_true == 1
# )

# N = np.sum(
#     y_true == 0
# )

# for threshold_value in thresholds:

#     prediction = (
#         scores >= threshold_value
#     ).astype(int)

#     tp_r = np.sum(
#         (prediction == 1)
#         & (y_true == 1)
#     )

#     fp_r = np.sum(
#         (prediction == 1)
#         & (y_true == 0)
#     )

#     tpr_list.append(
#         tp_r / P
#         if P
#         else 0
#     )

#     fpr_list.append(
#         fp_r / N
#         if N
#         else 0
#     )


# order = np.argsort(
#     fpr_list
# )

# fpr = np.array(
#     fpr_list
# )[order]

# tpr = np.array(
#     tpr_list
# )[order]


# if hasattr(np, "trapezoid"):

#     roc_auc = np.trapezoid(
#         tpr,
#         fpr
#     )

# else:

#     roc_auc = np.trapz(
#         tpr,
#         fpr
#     )


# plt.figure(figsize=(8, 6))

# plt.plot(
#     fpr,
#     tpr,
#     linewidth=2,
#     label=f"ROC Curve (AUC = {roc_auc:.4f})"
# )

# plt.plot(
#     [0, 1],
#     [0, 1],
#     linestyle="--",
#     label="Random Classifier"
# )

# plt.xlabel("False Positive Rate")
# plt.ylabel("True Positive Rate")

# plt.title(
#     "Receiver Operating Characteristic (ROC)"
# )

# plt.legend(
#     loc="lower right"
# )

# plt.grid(True)

# plt.tight_layout()

# plt.show()

# print(
#     "ROC-AUC:",
#     round(roc_auc, 4)
# )


# # ============================================================
# # 14. PREDICTED PROBABILITY DISTRIBUTION
# # ============================================================

# approved_prob = scores[
#     y_true == 1
# ]

# not_approved_prob = scores[
#     y_true == 0
# ]

# plt.figure(figsize=(9, 5))

# bins = np.linspace(
#     0,
#     1,
#     11
# )

# plt.hist(
#     not_approved_prob,
#     bins=bins,
#     alpha=0.65,
#     label="Not Approved"
# )

# plt.hist(
#     approved_prob,
#     bins=bins,
#     alpha=0.65,
#     label="Approved"
# )

# plt.axvline(
#     0.5,
#     linestyle="--",
#     linewidth=2,
#     label="Decision Threshold = 0.5"
# )

# plt.xlabel("Predicted Probability")
# plt.ylabel("Frequency")

# plt.title(
#     "Distribution of Predicted Probabilities"
# )

# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()


# # ============================================================
# # 15. DECISION BOUNDARY
# # ============================================================

# income_min = X[:, 0].min()
# income_max = X[:, 0].max()

# credit_min = X[:, 2].min()
# credit_max = X[:, 2].max()

# grid_income = np.linspace(
#     income_min,
#     income_max,
#     180
# )

# grid_credit = np.linspace(
#     credit_min,
#     credit_max,
#     180
# )

# GI, GC = np.meshgrid(
#     grid_income,
#     grid_credit
# )

# fixed_age = float(
#     np.median(
#         X_test[:, 1]
#     )
# )

# grid_input = np.column_stack([
#     GI.ravel(),
#     np.full(
#         GI.size,
#         fixed_age
#     ),
#     GC.ravel()
# ])

# grid_probability = (
#     model.predict_proba(
#         grid_input
#     )
#     .reshape(GI.shape)
# )

# plt.figure(figsize=(9, 6))

# plt.contourf(
#     GI,
#     GC,
#     grid_probability,
#     levels=np.linspace(
#         0,
#         1,
#         21
#     ),
#     alpha=0.45
# )

# plt.contour(
#     GI,
#     GC,
#     grid_probability,
#     levels=[0.5],
#     linewidths=2
# )

# test_class_0 = (
#     y_true == 0
# )

# test_class_1 = (
#     y_true == 1
# )

# plt.scatter(
#     X_test[test_class_0, 0],
#     X_test[test_class_0, 2],
#     marker="o",
#     edgecolors="black",
#     label="Actual: Not Approved"
# )

# plt.scatter(
#     X_test[test_class_1, 0],
#     X_test[test_class_1, 2],
#     marker="o",
#     edgecolors="black",
#     label="Actual: Approved"
# )

# plt.xlabel("Income (Normalized)")
# plt.ylabel("Credit Score (Normalized)")

# plt.title(
#     "Neural Network Decision Boundary"
# )

# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()


# # ============================================================
# # 16. FINAL ANALYSIS
# # ============================================================

# print("\n========================================")
# print("FINAL MODEL ANALYSIS")
# print("========================================")

# print(
#     f"Test Accuracy : {accuracy * 100:.2f}%"
# )

# print(
#     f"Precision : {precision * 100:.2f}%"
# )

# print(
#     f"Recall : {recall * 100:.2f}%"
# )

# print(
#     f"Specificity : {specificity * 100:.2f}%"
# )

# print(
#     f"F1 Score : {f1 * 100:.2f}%"
# )

# print(
#     f"MSE : {mse:.6f}"
# )

# print(
#     f"ROC-AUC : {roc_auc:.4f}"
# )

# print("\nConfusion Matrix:")
# print(cm)


import numpy as np
# Generate dataset
np.random.seed(42)
n = 100
study_hours = np.random.randint(1, 11, n)
attendance = np.random.randint(30, 101, n)
# Generate expected output
score = 0.6 * (study_hours / 10) + 0.4 * (attendance / 100)
Y = (score >= 0.55).astype(int).reshape(-1, 1)
# Input data
X = np.column_stack((study_hours, attendance))
# Normalize inputs
X = X / np.array([10, 100])
# Initialize weights and biases
W1 = np.random.rand(2, 2)
W2 = np.random.rand(2, 1)
b1 = np.zeros((1, 2))
b2 = np.zeros((1, 1))
learning_rate = 0.5
epochs = 20000
# Sigmoid activation function
def sigmoid(x):
    return X / (1 + np.exp(-x))
# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)
# Training using backpropagation
for epoch in range(epochs):
    # Forward propagation
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)
    # Calculate output error
    error = Y - predicted_output
    # Backward propagation
    output_delta = error * sigmoid_derivative(predicted_output)
    hidden_error = np.dot(output_delta, W2.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
    # Update weights and biases
    W2 += learning_rate * np.dot(hidden_output.T, output_delta)
    b2 += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    W1 += learning_rate * np.dot(X.T, hidden_delta)
    b1 += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)
# Testing
print("Study Hours | Attendance | Expected | Predicted")
print("-----------------------------------------------")
for i in range(len(X)):
    hidden = sigmoid(np.dot(X[i], W1) + b1)
    output = sigmoid(np.dot(hidden, W2) + b2)
    result = 1 if output[0][0] >= 0.5 else 0
    print(
        study_hours[i], "       ",
        attendance[i], "       ",
        Y[i][0], "        ",
        result
    )


