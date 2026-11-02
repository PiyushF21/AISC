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
A = 2*A-1
B=2*B-1
A=A.flatten()
B=B.flatten()
W= np.outer(A,B)
damaged = A.copy()
damaged[[1,5,10,16,22]]*=-1
output = damaged.copy()
for i in range(25):
    net = 0
    for j in range(25):
        net+=damaged[i]*W[j][i]
    if net>=0:
        output[i]=1
    else:
        output[i]=-1

