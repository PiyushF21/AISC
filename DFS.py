A = 4
B = 3
goal = 2

def isGoal(state):
    x, y = state
    return x == goal or y == goal


def get_Neighbours(state):
    x, y = state
    neighbours = []

    neighbours.append((A, y))
    neighbours.append((x, B))
    neighbours.append((0, y))
    neighbours.append((x, 0))

    transfer = min(x, B-y)
    neighbours.append((x-transfer, y+transfer))

    transfer = min(y, A-x)
    neighbours.append((x+transfer, y-transfer))

    return neighbours


def dfs(start):
    stack = [(start, [start])]
    visited = {start}

    while stack:
        state, path = stack.pop()

        if isGoal(state):
            return path

        for neighbour in get_Neighbours(state):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append((neighbour, path+[neighbour]))

    return None


start = (0, 0)
result = dfs(start)

if result:
    for state in result:
        print(state)