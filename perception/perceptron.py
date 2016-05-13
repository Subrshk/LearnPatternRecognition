class perceptron:
    def __init__(self, dataSet, rate):
        self.dataSet = dataSet
        self.rate = rate
        self.w = [0] * len(dataSet[0])
        self.b = 0
    def update(self, item):
        print("update at", item, end="")
        for x in enumerate(item[0]):
            self.w[x[0]] += item[1] * x[1]
        self.b += item[1]
        print("\tw =", self.w, "\tb =", self.b)

    def sign(self, item):
        return item[1]*(sum(self.rate*x*y for x, y in zip(item[0], self.w)) + self.b)
    def runOneTurn(self):
        falg = False
        for item in self.dataSet:
            if self.sign(item) <= 0:
                self.update(item)
                falg = True
        return falg
    def run(self):
        for i in range(1000):
            if not self.runOneTurn():
                break
        print(self.w, self.b)

if __name__ == '__main__':

    dataSet = [[[3, 3], 1], [[1, 1], -1], [[4, 3], 1]]
    per = perceptron(dataSet, 1)
    per.run()
