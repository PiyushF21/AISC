import numpy as np
X = np.array([[0.5,0.8]])
Y = np.array([[1]])
w1=np.array([[0.2,0.4],[0.3,0.5]])
w2=np.array([[0.6],[0.7]])
b1 = b1=np.zeros((1,2))
b2=np.zeros((1,1))

def sigmoid(X):
    return X/(1+np.exp(-X))

def sigmoid_derivative(X):
    return X*(1-X)

epochs = 1000
learning_rate = 0.5
for epoch in range(epochs):
    hidden_input = np.dot(X,w1)+b1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output,w2)+b2
    predicted = sigmoid(final_input)
    error = Y-predicted
    output_delta=error*sigmoid_derivative(predicted)
    hidden_error=np.dot(output_delta,w2.T)
    hidden_delta=hidden_error*sigmoid_derivative(hidden_output)
    w2+= learning_rate*np.dot(hidden_output.T,output_delta) 
    b2+= learning_rate*np.sum(output_delta,axis=0,keepdims=True)
    w1+= learning_rate*np.dot(X.T,hidden_delta)
    b1+= learning_rate*np.sum(hidden_delta,axis=0,keepdims=True)

print("X Y Predicted")
hidden_output = sigmoid(np.dot(X,w1)+b1)
predicted = sigmoid(np.dot(hidden_output,w2)+b2)
print(X,Y,predicted)
