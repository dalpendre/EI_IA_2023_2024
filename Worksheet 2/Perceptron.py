import numpy as np

class Perceptron:
    def __init__(self):
        self.w = None
        self.b = None

    def fit(self, xx: np.ndarray, yy: np.ndarray, learning_rate: float = 0.1, seed: int = 1) -> None:
        num_features = xx.shape[1]
        rng = np.random.default_rng(seed)
        self.w = rng.random(num_features)
        self.b = rng.random()

        change = True
        while change:
            change = False
            for i, x in enumerate(xx):
                a = self.predict(xx[i])
                print(str(x) + ' ' + str(a))
                print("--------------------")

                if a != yy[i]:
                    change = True
                    update = learning_rate * (yy[i] - a)
                    self.w = update * x
                    self.b += update

    def predict(self, x: np.ndarray) -> int:
        weightSum = np.dot(x, self.w) + self.b
        return 1 if weightSum > 0.0 else -1