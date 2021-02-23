import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],3) 
        self.weights2   = 2 * np.random.random((3,1)) - 1                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = self.out(self.layer1)
        
    def out(self,inputs):
        
        inputs = inputs.astype(float)
        output = sigmoid(np.dot(inputs, self.weights2))
        
        return output

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.out(self.layer1))))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
class NeuralNetwork2:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],3) 
        self.weights2   = 2 * np.random.random((3,1)) - 1                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = self.out(self.layer1)
        
    def out(self,inputs):
        
        inputs = inputs.astype(float)
        output = sigmoid(np.dot(inputs, self.weights2))
        
        return output

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.out(self.layer1))))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
class NeuralNetwork3:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],3) 
        self.weights2   = 2 * np.random.random((3,1)) - 1                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = self.out(self.layer1)
        
    def out(self,inputs):
        
        inputs = inputs.astype(float)
        output = sigmoid(np.dot(inputs, self.weights2))
        
        return output

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.out(self.layer1))))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


if __name__ == "__main__":
    X = np.array([[0,0,1],
                  [0,1,0],
                  [1,0,0]])
    y = np.array([[0],[1],[0]])
    y2 = np.array([[1],[0],[0]])
    y3 = np.array([[0],[0],[1]])
    
    nn = NeuralNetwork(X,y)
    nn2 = NeuralNetwork2(X,y2)
    nn3 = NeuralNetwork3(X,y3)
    def run():
           
        for i in range(2000):
            nn.feedforward()
            nn.backprop()
            nn2.feedforward()
            nn2.backprop()
            nn3.feedforward()
            nn3.backprop()
    run()
    print(nn.output)
    print(nn2.output)
    print(nn3.output)
    
    
    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))
    l = np.array([user_input_one, user_input_two, user_input_three])
    print(l)
    l = l.astype(float)
    print(l)
    while True:
        user_input_one = str(input("User Input One: "))
        user_input_two = str(input("User Input Two: "))
        user_input_three = str(input("User Input Three: "))
        print(nn.out(np.array([user_input_one, user_input_two, user_input_three])))
        print(nn2.out(np.array([user_input_one, user_input_two, user_input_three])))
        print(nn3.out(np.array([user_input_one, user_input_two, user_input_three])))
    
    
    