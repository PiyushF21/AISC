import numpy as np

# ---------------------------------------------------------
# 1. DISEASE PATTERNS
# ---------------------------------------------------------
# Diseases:
# Flu, Cold, Malaria
#
# Features:
# Fever, Cough, Fatigue, Sneezing, Chills, Headache

diseases = np.array([
    [1,  1,  1, -1, -1, -1],   # Flu
    [-1, 1, -1,  1, -1, -1],    # Cold
    [1, -1, -1, -1,  1,  1]     # Malaria
])

# ---------------------------------------------------------
# 2. SYMPTOM PATTERNS
# ---------------------------------------------------------

symptoms = np.array([
    [1,  1,  1, -1, -1, -1],   # Flu symptoms
    [-1, 1, -1,  1, -1, -1],    # Cold symptoms
    [1, -1, -1, -1,  1,  1]     # Malaria symptoms
])

# ---------------------------------------------------------
# 3. CREATE BAM WEIGHT MATRIX
# ---------------------------------------------------------

W = np.zeros((6, 6))

for i in range(len(diseases)):
    W += np.outer(diseases[i], symptoms[i])

print("BAM Weight Matrix:")
print(W)

# ---------------------------------------------------------
# 4. ACTIVATION FUNCTION
# ---------------------------------------------------------

def bipolar_activation(x):
    if x >= 0:
        return 1
    else:
        return -1

# ---------------------------------------------------------
# 5. DISEASE → SYMPTOMS
# ---------------------------------------------------------

def disease_to_symptoms(disease):

    symptoms_result = np.dot(disease, W)

    symptoms_result = np.array([
        bipolar_activation(x)
        for x in symptoms_result
    ])

    return symptoms_result

# ---------------------------------------------------------
# 6. SYMPTOMS → DISEASE
# ---------------------------------------------------------

def symptoms_to_disease(symptom):

    disease_result = np.dot(symptom, W.T)

    disease_result = np.array([
        bipolar_activation(x)
        for x in disease_result
    ])

    return disease_result

# ---------------------------------------------------------
# 7. TEST DISEASE → SYMPTOMS
# ---------------------------------------------------------

disease_names = ["Flu", "Cold", "Malaria"]

print("\nDisease → Symptoms")

for i in range(len(diseases)):

    result = disease_to_symptoms(diseases[i])

    print("\nDisease:", disease_names[i])
    print("Input Disease Pattern :", diseases[i])
    print("Retrieved Symptoms    :", result)

# ---------------------------------------------------------
# 8. TEST SYMPTOMS → DISEASE
# ---------------------------------------------------------

print("\nSymptoms → Disease")

for i in range(len(symptoms)):

    result = symptoms_to_disease(symptoms[i])

    print("\nInput Symptoms :", symptoms[i])

    # Compare retrieved pattern with diseases
    similarities = []

    for disease in diseases:
        similarity = np.sum(result == disease)
        similarities.append(similarity)

    predicted_index = np.argmax(similarities)

    print("Predicted Disease:", disease_names[predicted_index])




import numpy as np

# Pattern A
A = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
])

# Pattern B
B = np.array([
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0]
])

# Convert 0/1 to -1/+1
A = 2 * A - 1
B = 2 * B - 1

# Flatten patterns
A = A.flatten()
B = B.flatten()

# Create weight matrix
W = np.zeros((25, 25))
W = np.outer(A,B)
# for i in range(25):
#     for j in range(25):
#         W[i][j] = A[i] * B[j]

# Create damaged pattern A
damaged = A.copy()
damaged[[1, 5, 10, 16, 22]] *= -1

# A -> B
output = np.zeros(25)

for j in range(25):
    net = 0

    for i in range(25):
        net += damaged[i] * W[i][j]

    if net >= 0:
        output[j] = 1
    else:
        output[j] = -1

# B -> A
recalled_A = np.zeros(25)
for i in range(25):
    net = 0
    for j in range(25):
        net += output[j] * W[i][j]
    if net >= 0:
        recalled_A[i] = 1
    else:
        recalled_A[i] = -1
# Convert back to images
input_image = (damaged.reshape(5, 5) + 1) // 2
output_image = (output.reshape(5, 5) + 1) // 2
recalled_image = (recalled_A.reshape(5, 5) + 1) // 2
# Display results
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 3))
plt.subplot(1, 3, 1)
plt.imshow(input_image, cmap='gray')
plt.title("Input A")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(output_image, cmap='gray')
plt.title("Retrieved B")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(recalled_image, cmap='gray')
plt.title("Retrieved A")
plt.axis("off")
plt.show()