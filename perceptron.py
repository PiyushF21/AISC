def activation(total):
    if total>=0:
        return 1
    return 0

X = [[0,0],[0,1],[1,0],[1,1]]
Y = [0,0,0,1]
W=[0,0]
B=0

epochs = 10
learning_rate = 1
for epoch in range(epochs):
    for i in range(len(X)):
        total = 0
        for j in range(len(W)):
            total+=X[i][j]*W[j]
        total+=B
        predicted =activation(total)
        error = Y[i]-predicted
        for j in range(len(W)):
            W[j]+=learning_rate*error*X[i][j]
        B+=learning_rate*error


for i in range(len(X)):
        total = 0
        for j in range(len(W)):
            total+=X[i][j]*W[j]
        total+=B
        predicted =activation(total)
        print(X[i][0],X[i][1],Y[i],predicted) 