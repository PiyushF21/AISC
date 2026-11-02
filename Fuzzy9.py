import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True)

# 1. FUZZY SETS

rooms = ["Room 1", "Room 2", "Room 3"]

A = np.array([0.8, 0.5, 0.2])  # Hot Temperature
B = np.array([0.7, 0.5, 0.3])  # High Humidity

temperature = np.array([0.8, 0.5, 0.2])
humidity = np.array([0.7, 0.5, 0.3])
cooling = np.array([0.2, 0.5, 0.9])

temp_names = ["Cool", "Comfortable", "Hot"]
humidity_names = ["Low", "Moderate", "High"]
cooling_names = ["Low", "Medium", "High"]

print("FUZZY SET A:", A)
print("FUZZY SET B:", B)


# 2. FUZZY SET OPERATIONS

union = np.maximum(A, B)
intersection = np.minimum(A, B)

algebraic_sum = A + B - A * B
algebraic_product = A * B

bounded_sum = np.minimum(A + B, 1)
bounded_difference = np.maximum(A - B, 0)

print("\nUNION:", union)
print("INTERSECTION:", intersection)
print("ALGEBRAIC SUM:", algebraic_sum)
print("ALGEBRAIC PRODUCT:", algebraic_product)
print("BOUNDED SUM:", bounded_sum)
print("BOUNDED DIFFERENCE:", bounded_difference)


# 3. FUZZY CARTESIAN PRODUCT

R = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        R[i][j] = min(temperature[i], humidity[j])

print("\nFUZZY CARTESIAN PRODUCT:")
print(R)


# 4. SECOND FUZZY RELATION

S = np.array([
    [0.2, 0.4, 0.8],
    [0.3, 0.6, 0.8],
    [0.7, 0.8, 0.9]
])

print("\nSECOND FUZZY RELATION:")
print(S)


# 5. MAX-MIN COMPOSITION

max_min = np.zeros((3, 3))

for i in range(3):
    for k in range(3):
        maximum = 0

        for j in range(3):
            value = min(R[i][j], S[j][k])

            if value > maximum:
                maximum = value

        max_min[i][k] = maximum

print("\nMAX-MIN COMPOSITION:")
print(max_min)


# 6. MAX-PRODUCT COMPOSITION

max_product = np.zeros((3, 3))

for i in range(3):
    for k in range(3):
        maximum = 0

        for j in range(3):
            value = R[i][j] * S[j][k]

            if value > maximum:
                maximum = value

        max_product[i][k] = maximum

print("\nMAX-PRODUCT COMPOSITION:")
print(max_product)


# 7. GRAPH 1 - FUZZY SETS

plt.figure(figsize=(7, 4))

plt.plot(temp_names, temperature, marker='o', label="Temperature")
plt.plot(humidity_names, humidity, marker='s', label="Humidity")
plt.plot(cooling_names, cooling, marker='^', label="Cooling")

plt.title("Fuzzy Sets")
plt.ylabel("Membership Value")
plt.ylim(0, 1)
plt.legend()
plt.grid()
plt.show()


# 8. GRAPH 2 - FUZZY OPERATIONS

plt.figure(figsize=(8, 4))

plt.plot(rooms, union, marker='o', label="Union")
plt.plot(rooms, intersection, marker='o', label="Intersection")
plt.plot(rooms, algebraic_sum, marker='o', label="Algebraic Sum")
plt.plot(rooms, algebraic_product, marker='o', label="Algebraic Product")
plt.plot(rooms, bounded_sum, marker='o', label="Bounded Sum")
plt.plot(rooms, bounded_difference, marker='o', label="Bounded Difference")

plt.title("Fuzzy Set Operations")
plt.ylabel("Membership Value")
plt.ylim(0, 1.1)
plt.legend()
plt.grid()
plt.show()


# 9. GRAPH 3 - COMPOSITION MATRICES

plt.figure(figsize=(9, 4))

plt.subplot(1, 2, 1)
plt.imshow(max_min, cmap="YlGnBu", vmin=0, vmax=1)
plt.title("Max-Min Composition")
plt.xticks(range(3), cooling_names)
plt.yticks(range(3), temp_names)
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(max_product, cmap="YlGnBu", vmin=0, vmax=1)
plt.title("Max-Product Composition")
plt.xticks(range(3), cooling_names)
plt.yticks(range(3), temp_names)
plt.colorbar()

plt.tight_layout()
plt.show()


# 10. RESULT

print("\nExperiment completed successfully.")
