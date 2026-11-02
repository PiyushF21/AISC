import numpy as np

X= np.array([[0.5,0.8]])
Y=np.array([[1]])
w1=np.array([[0.2,0.4],[0.3,0.5]])
w2=np.array([0.6],[0.7])
b1=np.zeros((2,2))
b2=np.zeros((1,2))

def sigmoid(X):
    return X/(1+np.exp(-X))
def sigmoid_activation(X):
    return X*(1-X)
learning_rate = 0.5
epochs=1000
for i in range(epochs):
    hidden_input=np.dot(X,w1)+b1
    hidden_output=sigmoid(hidden_input)
    final_input = np.dot(hidden_output,w2)+b2
    predicted = sigmoid(final_input)
    error = Y-predicted
    output_delta=error*sigmoid_activation(predicted)
    hidden_error=np.dot(output_delta,w2.T)
    hidden_delta = hidden_error*sigmoid_activation(hidden_output)
    w2+=learning_rate*np.dot(hidden_output.T,output_delta) 
    b2+=learning_rate*np.sum(output_delta,axis=0,keepdims=True)
    w1+=learning_rate*np.dot(hidden_delta)
    b1+=learning_rate*np.sum(X.T,hidden_delta,axis=0,keepdims=True)
