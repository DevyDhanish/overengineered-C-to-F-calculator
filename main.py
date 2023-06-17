import numpy as np
import random

X_TRAIN = [[1], [77], [44], [99], [30], [12], [83], [73], [66], [13], [56], [58], [58], [37], [51], [72], [28], [57], [41], [69], [36], [71], [93], [17], 
           [70], [35], [31], [82], [37], [70], [87], [60], [78], [14], [48], [2], [18], [49], [97], [57], [66], [61], [65], [21], [9], [39], [68], [35], [95], [24]]

Y_TRAIN = [33.8, 170.6, 111.2, 210.2, 86.0, 53.6, 181.4, 163.4, 150.8, 55.4, 132.8, 136.4, 136.4, 98.6, 123.8, 161.6, 82.4, 134.6, 105.8, 156.2, 96.8, 159.8, 199.4, 62.6,
           158.0, 95.0, 87.8, 179.6, 98.6, 158.0, 188.6, 140.0, 172.4, 57.2, 118.4, 35.6, 64.4, 120.2, 206.6, 134.6, 150.8, 141.8, 149.0, 69.8, 48.2, 102.2, 154.4, 95.0, 203.0, 75.2]

SAVED_PRAMS = []

class Perceptron():
    def __init__(self) -> None:
        self.weights = []
        self.bias = 0.5
        self.loss = []
        self.mse_loss = 0

    def get_weighted_sum(self, inputs):
        output = 0
        for i in range(len(inputs)):
            output += inputs[i] * self.weights[i]
        return output + self.bias

    def activation_function(self, x):
        #return 1 / (1 + np.exp(-x))
        return x/1000

    def train(self, x_train, y_train, epochs, learning_rate):
        for i in range(len(x_train[0])):
            self.weights.append(random.uniform(0, 1))
            #self.weights.append(0)

        for iteration in range(epochs):
            self.loss = []
            for i in range(len(x_train)):
                weighted_sum = self.get_weighted_sum(x_train[i])
                predicted_ouput = self.activation_function(weighted_sum)
                difference = y_train[i] - predicted_ouput
                self.loss.append(difference * difference)

                for w in range(len(self.weights)):
                    self.weights[w] = self.weights[w] + learning_rate * difference * x_train[i][w]

                self.bias = self.bias + learning_rate * difference

            self.mse_loss = np.mean(self.loss)

            print(f"epoch {iteration} loss {self.mse_loss} weights {self.weights} bias {self.bias}")
        
        SAVED_PRAMS.append(self.weights)
        SAVED_PRAMS.append(self.bias)

    def predict(self, inputs):
        output = 0
        for i in range(len(SAVED_PRAMS[0])):
            output += inputs * SAVED_PRAMS[0][i]

        return self.activation_function(output + SAVED_PRAMS[1])



model = Perceptron()
model.train(X_TRAIN, Y_TRAIN, 50000, 0.01)

while(True):
    C = int(input("Enter celsius - "))
    print(f"{C} celsius in  fahrenheit is {model.predict(C)}")