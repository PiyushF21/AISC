# def get_next_states(state, cap_a, cap_b):
#     a, b = state
#     states = []

#     # Fill Jug A
#     states.append(((cap_a, b), "Fill Jug A"))

#     # Fill Jug B
#     states.append(((a, cap_b), "Fill Jug B"))

#     # Empty Jug A
#     states.append(((0, b), "Empty Jug A"))

#     # Empty Jug B
#     states.append(((a, 0), "Empty Jug B"))

#     # Pour A -> B
#     amount = min(a, cap_b - b)
#     states.append(((a - amount, b + amount), "Pour Jug A -> Jug B"))

#     # Pour B -> A
#     amount = min(b, cap_a - a)
#     states.append(((a + amount, b - amount), "Pour Jug B -> Jug A"))

#     return states

# def depth_limited_search(state, target, cap_a, cap_b, depth, path, visited):

#     a, b = state

#     if a == target or b == target:
#         return path

#     if depth == 0:
#         return None

#     visited.add(state)

#     for next_state, action in get_next_states(state, cap_a, cap_b):

#         if next_state not in visited:
#             result = depth_limited_search(
#                 next_state,
#                 target,
#                 cap_a,
#                 cap_b,
#                 depth - 1,
#                 path + [(action, next_state)],
#                 visited
#             )

#             if result is not None:
#                 return result

#     visited.remove(state)

#     return None

# def iddfs(cap_a, cap_b, target):

#     for depth in range(50):

#         path = depth_limited_search(
#             (0, 0),
#             target,
#             cap_a,
#             cap_b,
#             depth,
#             [("Start", (0, 0))],
#             set()
#         )

#         if path is not None:
#             return path

#     return None

# cap_a = int(input("Enter capacity of Jug A: "))
# cap_b = int(input("Enter capacity of Jug B: "))
# target = int(input("Enter target amount: "))

# if target > max(cap_a, cap_b):
#     print("Target cannot be achieved.")
# else:

#     solution = iddfs(cap_a, cap_b, target)

#     if solution is None:
#         print("No solution exists.")

#     else:
#         print("\nSolution found!\n")

#         for i, (action, state) in enumerate(solution):
#             print("Step", i, ":", action)
#             print(" Jug A =", state[0], "Jug B =", state[1])





A = 4
B = 3
GOAL = 2

def is_goal(state):
    x, y = state
    return x == GOAL or y == GOAL


def get_neighbors(state):
    x, y = state

    neighbors = []

    # 1. Fill A
    neighbors.append((A, y))

    # 2. Fill B
    neighbors.append((x, B))

    # 3. Empty A
    neighbors.append((0, y))

    # 4. Empty B
    neighbors.append((x, 0))

    # 5. Pour A into B
    transfer = min(x, B - y)
    neighbors.append((x - transfer, y + transfer))

    # 6. Pour B into A
    transfer = min(y, A - x)
    neighbors.append((x + transfer, y - transfer))

    return neighbors

from collections import deque

def bfs(start):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:

        state, path = queue.popleft()

        if is_goal(state):
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


start = (0, 0)

result = bfs(start)

if result:
    for state in result:
        print(state)
else:
    print("No solution")
