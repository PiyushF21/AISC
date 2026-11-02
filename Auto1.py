import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
])
A = 2*A-1
A=A.flatten()
W=np.outer(A,A)
np.fill_diagonal(W,0)
damaged = A.copy()
damaged[[1,5,10,16,22]]*=-1
output = damaged.copy()
for i in range(10):
    old = output.copy()
    for j in range(25):
        net = np.dot(W[j],output)
        if net>=0:
            output[j]=1
        else:
            output[j]=-1
    if np.array_equal(old,output):
        break

original = (A.reshape(5,5)+1)//2
damaged = (damaged.reshape(5,5)+1)//2
restored=(output.reshape(5,5)+1)//2

plt.figure(figsize=(9,3))
plt.subplot(1,3,1)
plt.imshow(original,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(damaged,cmap='gray')
plt.title('damaged')
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(restored,cmap='gray')
plt.title('restored')
plt.axis('off')

plt.show()