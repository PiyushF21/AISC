# import numpy as np
# import matplotlib.pyplot as plt

# # ---------------------------------------------------------
# # 1. HANDWRITTEN CHARACTER PATTERNS
# # ---------------------------------------------------------

# # Character A represented using 0 and 1
# A = np.array([
#     [0, 1, 1, 1, 0],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1]
# ])

# # Character B
# B = np.array([
#     [1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 0]
# ])

# # Convert 0/1 to -1/+1
# A = 2 * A - 1
# B = 2 * B - 1

# # Flatten the patterns
# A = A.flatten()
# B = B.flatten()

# # ---------------------------------------------------------
# # 2. CREATE WEIGHT MATRIX
# # ---------------------------------------------------------

# # Store both characters
# W = np.outer(A, A) + np.outer(B, B)

# # No self-connections
# np.fill_diagonal(W, 0)

# # ---------------------------------------------------------
# # 3. CREATE DAMAGED CHARACTER
# # ---------------------------------------------------------

# damaged_A = A.copy()

# # Introduce noise by flipping pixels
# noise_positions = [1, 5, 10, 16, 22]

# for position in noise_positions:
#     damaged_A[position] *= -1

# # ---------------------------------------------------------
# # 4. RESTORE CHARACTER
# # ---------------------------------------------------------

# state = damaged_A.copy()

# for iteration in range(10):

#     old_state = state.copy()

#     for i in range(len(state)):

#         activation = np.dot(W[i], state)

#         if activation >= 0:
#             state[i] = 1
#         else:
#             state[i] = -1

#     # Stop when pattern becomes stable
#     if np.array_equal(old_state, state):
#         break

# # ---------------------------------------------------------
# # 5. CONVERT BACK TO IMAGE
# # ---------------------------------------------------------

# original_image = A.reshape(5, 5)
# damaged_image = damaged_A.reshape(5, 5)
# restored_image = state.reshape(5, 5)

# # Convert -1/+1 to 0/1
# original_image = (original_image + 1) // 2
# damaged_image = (damaged_image + 1) // 2
# restored_image = (restored_image + 1) // 2

# # ---------------------------------------------------------
# # 6. DISPLAY RESULTS
# # ---------------------------------------------------------

# plt.figure(figsize=(9, 3))

# plt.subplot(1, 3, 1)
# plt.imshow(original_image, cmap="gray")
# plt.title("Original Character A")
# plt.axis("off")

# plt.subplot(1, 3, 2)
# plt.imshow(damaged_image, cmap="gray")
# plt.title("Damaged Character")
# plt.axis("off")

# plt.subplot(1, 3, 3)
# plt.imshow(restored_image, cmap="gray")
# plt.title("Restored Character")
# plt.axis("off")

# plt.tight_layout()
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt

# # Original pattern (A)
# A = np.array([
#     [0, 1, 1, 1, 0],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1]
# ])

# # Convert 0 and 1 into -1 and +1
# A = 2 * A - 1

# # Flatten pattern
# A = A.flatten()

# # Create weight matrix
# W = np.outer(A, A)

# # Remove self-connections
# np.fill_diagonal(W, 0)

# # Create damaged pattern
# damaged = A.copy()
# damaged[[1, 5, 10, 16, 22]] *= -1

# # Restore pattern
# output = damaged.copy()

# for k in range(10):
#     old = output.copy()

#     for i in range(25):
#         net = np.dot(W[i], output)

#         if net >= 0:
#             output[i] = 1
#         else:
#             output[i] = -1

#     if np.array_equal(old, output):
#         break

# # Convert back to images
# original = (A.reshape(5, 5) + 1) // 2
# damaged = (damaged.reshape(5, 5) + 1) // 2
# restored = (output.reshape(5, 5) + 1) // 2

# # Display output
# plt.figure(figsize=(9, 3))

# plt.subplot(1, 3, 1)
# plt.imshow(original, cmap='gray')
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1, 3, 2)
# plt.imshow(damaged, cmap='gray')
# plt.title("Damaged")
# plt.axis("off")

# plt.subplot(1, 3, 3)
# plt.imshow(restored, cmap='gray')
# plt.title("Restored")
# plt.axis("off")

# plt.show()



import numpy as np 
import matplotlib.pyplot as plt

A = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
])

W = np.outer(A,A)
A = A.flatten()