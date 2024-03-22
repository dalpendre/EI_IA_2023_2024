import numpy as np
import Perceptron

if __name__ == "__main__":

    training_data = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
    training_labels = np.array([-1, -1, -1, 1])

    perception = Perceptron()
    perception.fit(training_data, training_labels, learning_rate=0.1)

    training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    training_labels = np.array([0, 1, 1, 1])