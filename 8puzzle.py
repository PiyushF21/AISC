import heapq

def heuristic(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count

def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0, "Move Up"),
        (1, 0, "Move Down"),
        (0, -1, "Move Left"),
        (0, 1, "Move Right")
    ]

    for dr, dc, action in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append((tuple(new_state), action))

    return neighbors

def a_star(start, goal):

    pq = []

    h = heuristic(start, goal)

    heapq.heappush(pq, (h, 0, start))

    parent = {}
    action_taken = {}

    cost = {start: 0}

    while pq:

        f, g, current = heapq.heappop(pq)

        if current == goal:

            path = []

            while current != start:
                path.append(
                    (action_taken[current], current)
                )

                current = parent[current]

            path.reverse()

            return path

        for next_state, action in get_neighbors(current):

            new_g = g + 1

            if next_state not in cost or new_g < cost[next_state]:

                cost[next_state] = new_g

                h = heuristic(next_state, goal)

                new_f = new_g + h

                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state)
                )

                parent[next_state] = current
                action_taken[next_state] = action

    return None

def print_board(state): 
    for i in range(0, 9, 3): 
        print( state[i], state[i + 1], state[i + 2] )

# ---------------- INPUT ----------------

print("Enter initial state (use 0 for blank):")

start = tuple(
    map(int, input().split())
)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

print("\nInitial State:")
print_board(start)

solution = a_star(start, goal)

if solution is None:

    print("No solution exists.")

else:

    print("\nSolution found!")
    print("Number of moves:", len(solution))

    current = start

    print("\nStep 0:")
    print_board(current)

    for i, (action, state) in enumerate(solution, 1):

        print(action)

        print("Step", i, ":")
        print_board(state)
