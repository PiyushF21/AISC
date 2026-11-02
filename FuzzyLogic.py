import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True)

# ==========================================================
# EXPERIMENT 9: FUZZY SETS AND FUZZY RELATIONS
# Case Study: Smart Home Temperature Control
# ==========================================================

print("=" * 70)
print("EXPERIMENT 8: FUZZY SETS AND FUZZY RELATIONS")
print("Case Study: Smart Home Temperature Control")
print("=" * 70)

# ==========================================================
# 1. DEFINE FUZZY SETS
# ==========================================================

# Common universe for fuzzy set operations
rooms = ["Room 1", "Room 2", "Room 3"]

A = np.array([0.8, 0.5, 0.2])  # Hot Temperature
B = np.array([0.7, 0.5, 0.3])  # High Humidity

# Category universes for fuzzy relations
temperature_categories = ["Cool", "Comfortable", "Hot"]
humidity_categories = ["Low", "Moderate", "High"]
cooling_categories = ["Low", "Medium", "High"]

temperature_set = np.array([0.8, 0.5, 0.2])
humidity_set = np.array([0.7, 0.5, 0.3])
cooling_set = np.array([0.2, 0.5, 0.9])

def display_set(name, universe, values):
    print(f"\n{name}")
    print("-" * 50)
    print(f"{'Element':<22}{'Membership Value':>18}")

    for element, value in zip(universe, values):
        print(f"{element:<22}{value:>18.2f}")

def display_matrix(title, matrix, rows, columns):
    print(f"\n{title}")
    print("-" * 65)
    print(f"{'':<16}" +
          "".join(f"{col:>16}" for col in columns))

    for name, row in zip(rows, matrix):
        print(f"{name:<16}" +
              "".join(f"{value:>16.2f}" for value in row))

display_set("FUZZY SET A: HOT TEMPERATURE", rooms, A)
display_set("FUZZY SET B: HIGH HUMIDITY", rooms, B)

display_set("FUZZY SET: TEMPERATURE CATEGORIES",
            temperature_categories, temperature_set)

display_set("FUZZY SET: HUMIDITY CATEGORIES",
            humidity_categories, humidity_set)

display_set("FUZZY SET: COOLING LEVEL",
            cooling_categories, cooling_set)

# ==========================================================
# 2. FUZZY SET OPERATIONS
# ==========================================================

# Union
union = np.maximum(A, B)

# Intersection
intersection = np.minimum(A, B)

# Algebraic Sum
algebraic_sum = A + B - A * B

# Algebraic Product
algebraic_product = A * B

# Bounded Sum
bounded_sum = np.minimum(A + B, 1)

# Bounded Difference A - B
bounded_difference = np.maximum(A - B, 0)

print("\n" + "=" * 70)
print("FUZZY SET OPERATIONS")
print("=" * 70)

print("Union              = max(A, B)")
print("Intersection       = min(A, B)")
print("Algebraic Sum      = A + B - A*B")
print("Algebraic Product  = A*B")
print("Bounded Sum        = min(A + B, 1)")
print("Bounded Difference = max(A - B, 0)")

print(f"\n{'Room':<15}{'A':>7}{'B':>7}"
      f"{'Union':>9}{'Intersect':>12}"
      f"{'Alg.Sum':>10}{'Alg.Prod':>10}"
      f"{'Bound.Sum':>12}{'Bound.Diff':>12}")

for i, room in enumerate(rooms):
    print(f"{room:<15}"
          f"{A[i]:>7.2f}"
          f"{B[i]:>7.2f}"
          f"{union[i]:>9.2f}"
          f"{intersection[i]:>12.2f}"
          f"{algebraic_sum[i]:>10.2f}"
          f"{algebraic_product[i]:>10.2f}"
          f"{bounded_sum[i]:>12.2f}"
          f"{bounded_difference[i]:>12.2f}")

# ==========================================================
# 3. FUZZY CARTESIAN PRODUCT
# R(i,j) = min(A(i), B(j))
# ==========================================================

R = np.minimum(
    temperature_set[:, None],
    humidity_set[None, :]
)

display_matrix(
    "FUZZY CARTESIAN PRODUCT R = TEMPERATURE x HUMIDITY",
    R,
    temperature_categories,
    humidity_categories
)

# ==========================================================
# 4. SECOND FUZZY RELATION
# Humidity -> Cooling Level
# Illustrative rule-based relation
# ==========================================================

S = np.array([
    [0.2, 0.4, 0.8],  # Low humidity
    [0.3, 0.6, 0.8],  # Moderate humidity
    [0.7, 0.8, 0.9]   # High humidity
])

display_matrix(
    "FUZZY RELATION S = HUMIDITY -> COOLING LEVEL",
    S,
    humidity_categories,
    cooling_categories
)

# ==========================================================
# 5. MAX-MIN COMPOSITION
# T(i,k) = max_j min(R(i,j), S(j,k))
# ==========================================================

max_min = np.zeros((3, 3))

for i in range(3):
    for k in range(3):
        values = [
            min(R[i, j], S[j, k])
            for j in range(3)
        ]
        max_min[i, k] = max(values)

display_matrix(
    "MAX-MIN COMPOSITION: R o S",
    max_min,
    temperature_categories,
    cooling_categories
)

# ==========================================================
# 6. MAX-PRODUCT COMPOSITION
# T(i,k) = max_j [R(i,j) * S(j,k)]
# ==========================================================

max_product = np.zeros((3, 3))

for i in range(3):
    for k in range(3):
        values = [
            R[i, j] * S[j, k]
            for j in range(3)
        ]
        max_product[i, k] = max(values)

display_matrix(
    "MAX-PRODUCT COMPOSITION: R o S",
    max_product,
    temperature_categories,
    cooling_categories
)

# ==========================================================
# 7. GRAPH 1: ALL FUZZY SETS IN ONE GRAPH
# ==========================================================

plt.figure(figsize=(9, 5))

plt.plot(temperature_categories, temperature_set,
         marker="o", linewidth=2, label="Temperature")

plt.plot(humidity_categories, humidity_set,
         marker="s", linewidth=2, label="Humidity")

plt.plot(cooling_categories, cooling_set,
         marker="^", linewidth=2, label="Cooling Level")

plt.title("Fuzzy Sets for Smart Home Temperature Control")
plt.xlabel("Categories")
plt.ylabel("Membership Value")
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ==========================================================
# 8. GRAPH 2: ALL FUZZY OPERATIONS IN ONE GRAPH
# ==========================================================

operation_names = [
    "Union",
    "Intersection",
    "Algebraic Sum",
    "Algebraic Product",
    "Bounded Sum",
    "Bounded Difference"
]

operation_values = [
    union,
    intersection,
    algebraic_sum,
    algebraic_product,
    bounded_sum,
    bounded_difference
]

x = np.arange(len(rooms))
width = 0.12

plt.figure(figsize=(12, 6))

for i, (name, values) in enumerate(
        zip(operation_names, operation_values)):

    plt.bar(
        x + (i - 2.5) * width,
        values,
        width,
        label=name
    )

plt.title("Fuzzy Set Operations")
plt.xlabel("Rooms")
plt.ylabel("Membership Value")
plt.xticks(x, rooms)
plt.ylim(0, 1.1)
plt.legend(ncol=3)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ==========================================================
# 9. GRAPH 3: BOTH COMPOSITION MATRICES IN ONE FIGURE
# ==========================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, matrix, title in [
    (axes[0], max_min, "Max-Min Composition"),
    (axes[1], max_product, "Max-Product Composition")
]:

    image = ax.imshow(
        matrix,
        vmin=0,
        vmax=1,
        cmap="YlGnBu"
    )

    ax.set_xticks(range(3))
    ax.set_xticklabels(cooling_categories, rotation=20, ha="right")
    ax.set_yticks(range(3))
    ax.set_yticklabels(temperature_categories)

    ax.set_xlabel("Cooling Level")
    ax.set_ylabel("Temperature Category")
    ax.set_title(title)

    for i in range(3):
        for j in range(3):
            ax.text(
                j, i, f"{matrix[i, j]:.2f}",
                ha="center",
                va="center"
            )

fig.colorbar(
    image,
    ax=axes.tolist(),
    label="Membership Value",
    shrink=0.85
)

plt.suptitle("Fuzzy Relation Composition Matrices")
plt.tight_layout()
plt.show()

# ==========================================================
# 10. RESULT
# ==========================================================

print("\n" + "=" * 70)
print("RESULT")
print("=" * 70)
print("1. Fuzzy sets were defined.")
print("2. All six fuzzy set operations were performed.")
print("3. Fuzzy Cartesian product was calculated.")
print("4. Max-Min composition was performed.")
print("5. Max-Product composition was performed.")
print("6. Three separate figures were generated:")
print("   - All fuzzy sets")
print("   - All fuzzy operations")
print("   - Both composition matrices")
print("\nExperiment completed successfully.")
