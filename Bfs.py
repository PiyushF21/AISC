from collections import deque
A=4
B=3
goal =2
def isGoal(state):
    x,y=state
    if x==goal or y==goal:
        return True
    return False

def get_Neighbours(state):
    x,y = state
    neighbours = []
    neighbours.append((A,y))
    neighbours.append((x,B))
    neighbours.append((0,y))
    neighbours.append((x,0))
    transfer = min((x,B-y))
    neighbours.append((x-transfer,y+transfer))
    transfer = min((y,A-x))
    neighbours.append((x+transfer,y-transfer))
    return neighbours
        

def bfs(start):
    queue = deque([(start,[start])])
    visited = {start}
    while queue:
        state , path = queue.popleft()
        if isGoal(state):
            return path  
        for neighbour in get_Neighbours(state):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour,path+[neighbour]])

    return None

start = (0,0)
result = bfs(start)
if result:
    for state in result:
        print(state)
        