import numpy as np

# ------------------------------------------------
# Creating a synthetic dataset
# 3 classes, 20 points in each class
# Each sample contains 2 features
# ------------------------------------------------

np.random.seed(42)

# Generate points for the three groups
group_A = np.random.normal(
    loc=(0.2, 0.2),
    scale=0.06,
    size=(20, 2)
)

group_B = np.random.normal(
    loc=(0.8, 0.2),
    scale=0.06,
    size=(20, 2)
)

group_C = np.random.normal(
    loc=(0.5, 0.8),
    scale=0.06,
    size=(20, 2)
)

# Form the complete feature matrix
X = np.concatenate((group_A, group_B, group_C), axis=0)

# Assign a label to every group
Y = np.concatenate([
    np.zeros(20, dtype=int),
    np.ones(20, dtype=int),
    np.full(20, 2, dtype=int)
])

# Display basic information
print("Shape of Dataset:", X.shape)
print("Total Samples:", X.shape[0])
print("Total Features:", X.shape[1])
print("Total Classes:", np.unique(Y).size)
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, suppress=True)

# ============================================================
# DATA GENERATION
# ============================================================

np.random.seed(42)

# Three clusters with 20 observations each
cluster1 = np.random.normal([0.20, 0.20], 0.06, (20, 2))
cluster2 = np.random.normal([0.80, 0.20], 0.06, (20, 2))
cluster3 = np.random.normal([0.50, 0.80], 0.06, (20, 2))

X = np.concatenate((cluster1, cluster2, cluster3))

labels = np.array(
    [0 for _ in range(20)] +
    [1 for _ in range(20)] +
    [2 for _ in range(20)]
)

# ============================================================
# DISPLAY DATASET
# ============================================================

def show_data():

    print("\n================ DATASET INFORMATION ================")

    print("Dataset size :", X.shape)
    print("Samples      :", X.shape[0])
    print("Features     :", X.shape[1])
    print("Classes      :", np.unique(labels).size)

    print("\nSamples in each class:")
    for class_id in np.unique(labels):
        print("Class", class_id, ":", np.count_nonzero(labels == class_id))

    print("\nNo.\tFeature 1\tFeature 2\tClass")
    print("-" * 55)

    for idx, sample in enumerate(X):
        print(
            idx + 1,
            "\t",
            round(sample[0], 4),
            "\t\t",
            round(sample[1], 4),
            "\t\t",
            labels[idx]
        )

# ============================================================
# KOHONEN SELF ORGANIZING FEATURE MAP
# ============================================================

def run_kohonen():

    print("\n========== KOHONEN SELF ORGANIZING FEATURE MAP ==========")

    grid_rows = 2
    grid_cols = 2
    total_epochs = 6

    alpha = 0.5
    neighbourhood = 1

    print("\nSOM Configuration")
    print("Grid size          :", grid_rows, "x", grid_cols)
    print("Total neurons      :", grid_rows * grid_cols)
    print("Initial alpha      :", alpha)
    print("Initial radius     :", neighbourhood)
    print("Training epochs    :", total_epochs)

    # Initialize neuron weights
    np.random.seed(10)

    neuron_weights = np.random.uniform(
        0,
        1,
        size=(grid_rows, grid_cols, X.shape[1])
    )

    print("\nStarting neuron weights:")

    for r in range(grid_rows):
        for c in range(grid_cols):
            print(
                "Neuron", (r, c),
                "=>",
                neuron_weights[r, c]
            )

    training_error = []

    # --------------------------------------------------------
    # SOM TRAINING
    # --------------------------------------------------------

    for ep in range(total_epochs):

        accumulated_error = 0

        order = np.arange(X.shape[0])
        np.random.shuffle(order)

        print("\n--------------- Epoch", ep + 1, "---------------")

        for count, data_index in enumerate(order):

            sample = X[data_index]

            # Calculate distance of sample from every neuron
            distance_map = np.zeros((grid_rows, grid_cols))

            for r in range(grid_rows):
                for c in range(grid_cols):

                    difference = sample - neuron_weights[r, c]

                    distance_map[r, c] = np.sum(difference ** 2)

            # Best Matching Unit
            bmu = np.unravel_index(
                np.argmin(distance_map),
                distance_map.shape
            )

            bmu_r, bmu_c = bmu

            bmu_error = distance_map[bmu_r, bmu_c]
            accumulated_error += bmu_error

            # Display one complete calculation per epoch
            if count == 0:

                print("\nSample number :", data_index + 1)
                print("Input         :", sample)

                print("\nDistance map:")

                for r in range(grid_rows):
                    for c in range(grid_cols):
                        print(
                            "Neuron", (r, c),
                            "=",
                            round(distance_map[r, c], 6)
                        )

                print("\nBMU           :", bmu)
                print("Minimum distance :", round(bmu_error, 6))

            # ------------------------------------------------
            # Update BMU and neurons inside the neighbourhood
            # ------------------------------------------------

            for r in range(grid_rows):
                for c in range(grid_cols):

                    grid_dist = np.sqrt(
                        (r - bmu_r) ** 2 +
                        (c - bmu_c) ** 2
                    )

                    if grid_dist <= neighbourhood:

                        previous = neuron_weights[r, c].copy()

                        neuron_weights[r, c] = (
                            neuron_weights[r, c]
                            + alpha * (sample - neuron_weights[r, c])
                        )

                        if count == 0:
                            print("\nNeuron", (r, c), "updated")
                            print("Before :", previous)
                            print("After  :", neuron_weights[r, c])

        mean_error = accumulated_error / X.shape[0]
        training_error.append(mean_error)

        print(
            "\nAverage squared distance:",
            round(mean_error, 6)
        )

        # Learning rate decay
        previous_alpha = alpha
        alpha *= 0.5

        print(
            "Learning rate:",
            round(previous_alpha, 6),
            "->",
            round(alpha, 6)
        )

        # Reduce neighbourhood after third epoch
        if ep == 2:
            neighbourhood = 0
            print("Neighbourhood radius is now 0")

    # --------------------------------------------------------
    # FINAL WEIGHTS
    # --------------------------------------------------------

    print("\n================ FINAL SOM WEIGHTS ================")

    for r in range(grid_rows):
        for c in range(grid_cols):
            print(
                "Neuron", (r, c),
                "=",
                neuron_weights[r, c]
            )

    # --------------------------------------------------------
    # BMU MAPPING
    # --------------------------------------------------------

    print("\n================ SAMPLE - BMU MAPPING ================")

    for idx, sample in enumerate(X):

        distance_map = np.zeros((grid_rows, grid_cols))

        for r in range(grid_rows):
            for c in range(grid_cols):
                distance_map[r, c] = np.sum(
                    (sample - neuron_weights[r, c]) ** 2
                )

        best_neuron = np.unravel_index(
            np.argmin(distance_map),
            distance_map.shape
        )

        print(
            "Sample", idx + 1,
            "| Actual class =", labels[idx],
            "| BMU =", best_neuron
        )

    # --------------------------------------------------------
    # ERROR GRAPH
    # --------------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.plot(
        np.arange(1, total_epochs + 1),
        training_error,
        marker="o"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Average Squared Euclidean Distance")
    plt.title("Kohonen SOM Training Error")
    plt.xticks(np.arange(1, total_epochs + 1))
    plt.grid(True)

    plt.show()

    # --------------------------------------------------------
    # SOM VISUALIZATION
    # --------------------------------------------------------

    plt.figure(figsize=(8, 7))

    for class_id in np.unique(labels):

        class_points = X[labels == class_id]

        plt.scatter(
            class_points[:, 0],
            class_points[:, 1],
            s=70,
            label="Class " + str(class_id)
        )

    # Horizontal connections
    for r in range(grid_rows):
        for c in range(grid_cols - 1):

            plt.plot(
                neuron_weights[r, c:c + 2, 0],
                neuron_weights[r, c:c + 2, 1],
                linestyle="--"
            )

    # Vertical connections
    for r in range(grid_rows - 1):
        for c in range(grid_cols):

            plt.plot(
                neuron_weights[r:r + 2, c, 0],
                neuron_weights[r:r + 2, c, 1],
                linestyle="--"
            )

    # SOM neurons
    for r in range(grid_rows):
        for c in range(grid_cols):

            point = neuron_weights[r, c]

            plt.scatter(
                point[0],
                point[1],
                marker="X",
                s=250
            )

            plt.text(
                point[0] + 0.015,
                point[1] + 0.015,
                "N(" + str(r) + "," + str(c) + ")"
            )

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Kohonen Self Organizing Feature Map")
    plt.legend()
    plt.grid(True)

    plt.show()

    input("\nPress Enter to go back to the main menu...")

# ============================================================
# LEARNING VECTOR QUANTIZATION
# ============================================================

def run_lvq():

    print("\n================ LEARNING VECTOR QUANTIZATION ================")

    class_count = 3
    total_epochs = 6
    alpha = 0.5

    print("\nLVQ Parameters")
    print("Classes       :", class_count)
    print("Initial alpha :", alpha)
    print("Epochs        :", total_epochs)

    # One prototype/reference vector for every class
    reference_vectors = np.array([
        X[0].copy(),
        X[20].copy(),
        X[40].copy()
    ])

    reference_labels = np.array([0, 1, 2])

    print("\nInitial reference vectors:")

    for i in range(class_count):
        print(
            "Vector", i + 1,
            "| Class =", reference_labels[i],
            "| Value =", reference_vectors[i]
        )

    lvq_error = []

    # --------------------------------------------------------
    # LVQ TRAINING
    # --------------------------------------------------------

    for ep in range(total_epochs):

        total_distance = 0

        order = np.arange(X.shape[0])
        np.random.shuffle(order)

        print("\n--------------- Epoch", ep + 1, "---------------")

        for count, data_index in enumerate(order):

            sample = X[data_index]
            actual_class = labels[data_index]

            # Distance from every reference vector
            distances = np.zeros(class_count)

            for j in range(class_count):

                distances[j] = np.sqrt(
                    np.sum(
                        (sample - reference_vectors[j]) ** 2
                    )
                )

            # Select nearest reference vector
            best = np.argmin(distances)

            predicted_class = reference_labels[best]
            smallest_distance = distances[best]

            total_distance += smallest_distance

            if count == 0:

                print("\nSample number :", data_index + 1)
                print("Input vector  :", sample)
                print("Actual class  :", actual_class)

                print("\nDistances:")

                for j in range(class_count):
                    print(
                        "Vector", j + 1,
                        "| Class =", reference_labels[j],
                        "| Distance =",
                        round(distances[j], 6)
                    )

                print("\nWinning vector :", best + 1)
                print("Winning class  :", predicted_class)
                print(
                    "Minimum distance:",
                    round(smallest_distance, 6)
                )

            old_vector = reference_vectors[best].copy()

            # Correct class -> move prototype towards input
            if actual_class == predicted_class:

                reference_vectors[best] = (
                    reference_vectors[best]
                    + alpha * (sample - reference_vectors[best])
                )

                operation = "Moved towards input"

            # Wrong class -> move prototype away from input
            else:

                reference_vectors[best] = (
                    reference_vectors[best]
                    - alpha * (sample - reference_vectors[best])
                )

                operation = "Moved away from input"

            if count == 0:

                print("\nPrototype update")
                print("Old vector :", old_vector)
                print("Operation  :", operation)
                print("New vector :", reference_vectors[best])

        mean_distance = total_distance / X.shape[0]
        lvq_error.append(mean_distance)

        print(
            "\nAverage Euclidean distance:",
            round(mean_distance, 6)
        )

        # Learning-rate reduction
        old_alpha = alpha
        alpha *= 0.5

        print(
            "Learning rate:",
            round(old_alpha, 6),
            "->",
            round(alpha, 6)
        )

    # --------------------------------------------------------
    # FINAL REFERENCE VECTORS
    # --------------------------------------------------------

    print("\n================ FINAL REFERENCE VECTORS ================")

    for j in range(class_count):
        print(
            "Vector", j + 1,
            "| Class =", reference_labels[j],
            "| Value =", reference_vectors[j]
        )

    # --------------------------------------------------------
    # CLASSIFICATION
    # --------------------------------------------------------

    predicted = []

    print("\n================ PREDICTIONS ================")

    for idx, sample in enumerate(X):

        distances = np.zeros(class_count)

        for j in range(class_count):

            distances[j] = np.sqrt(
                np.sum(
                    (sample - reference_vectors[j]) ** 2
                )
            )

        winner = np.argmin(distances)

        predicted_class = reference_labels[winner]
        predicted.append(predicted_class)

        print(
            "Sample", idx + 1,
            "| Actual =", labels[idx],
            "| Predicted =", predicted_class
        )

    predicted = np.array(predicted)

    # --------------------------------------------------------
    # PERFORMANCE
    # --------------------------------------------------------

    correct_count = np.sum(predicted == labels)
    incorrect_count = len(labels) - correct_count

    accuracy = (correct_count / len(labels)) * 100

    print("\n================ LVQ PERFORMANCE ================")
    print("Total samples       :", len(labels))
    print("Correct predictions :", correct_count)
    print("Wrong predictions   :", incorrect_count)
    print("Accuracy            :", round(accuracy, 2), "%")

    # --------------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------------

    confusion_matrix = np.zeros(
        (class_count, class_count),
        dtype=int
    )

    for actual, prediction in zip(labels, predicted):
        confusion_matrix[actual, prediction] += 1

    print("\nConfusion Matrix:")
    print(confusion_matrix)

    # --------------------------------------------------------
    # LVQ ERROR GRAPH
    # --------------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.plot(
        np.arange(1, total_epochs + 1),
        lvq_error,
        marker="o"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Average Euclidean Distance")
    plt.title("LVQ Training Error")
    plt.xticks(np.arange(1, total_epochs + 1))
    plt.grid(True)

    plt.show()

    # --------------------------------------------------------
    # REFERENCE VECTOR GRAPH
    # --------------------------------------------------------

    plt.figure(figsize=(8, 7))

    for class_id in np.unique(labels):

        class_points = X[labels == class_id]

        plt.scatter(
            class_points[:, 0],
            class_points[:, 1],
            s=70,
            label="Class " + str(class_id)
        )

    for j in range(class_count):

        vector = reference_vectors[j]

        plt.scatter(
            vector[0],
            vector[1],
            marker="X",
            s=300
        )

        plt.text(
            vector[0] + 0.015,
            vector[1] + 0.015,
            "W" + str(j + 1)
        )

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("LVQ Final Reference Vectors")
    plt.legend()
    plt.grid(True)

    plt.show()

    # --------------------------------------------------------
    # CONFUSION MATRIX GRAPH
    # --------------------------------------------------------

    plt.figure(figsize=(6, 5))

    plt.imshow(
        confusion_matrix,
        interpolation="nearest"
    )

    plt.title("LVQ Confusion Matrix")
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")

    class_names = ["Class 0", "Class 1", "Class 2"]

    plt.xticks(
        range(class_count),
        class_names
    )

    plt.yticks(
        range(class_count),
        class_names
    )

    for row in range(class_count):
        for col in range(class_count):

            plt.text(
                col,
                row,
                confusion_matrix[row, col],
                ha="center",
                va="center"
            )

    plt.colorbar()
    plt.show()

    input("\nPress Enter to go back to the main menu...")

# ============================================================
# MAIN PROGRAM
# ============================================================

def start_program():

    while True:

        print("\n")
        print("================================================")
        print("              EXPERIMENT 7")
        print("       UNSUPERVISED LEARNING ALGORITHMS")
        print("================================================")

        print("\n1 -> Display Dataset")
        print("2 -> Execute Kohonen SOFM")
        print("3 -> Execute Learning Vector Quantization")
        print("4 -> Exit")

        option = input("\nSelect an option: ")

        if option == "1":

            show_data()

            input("\nPress Enter to continue...")

        elif option == "2":

            run_kohonen()

        elif option == "3":

            run_lvq()

        elif option == "4":

            print("\nExperiment 7 completed.")
            print("Program ended.")

            break

        else:

            print("\nInvalid option. Please try again.")

            input("Press Enter to continue...")

start_program()