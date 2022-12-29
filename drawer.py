import matplotlib.pyplot as plt

class animator():
    def __init__(self,x_t, names):
        self.x_t = x_t
        self.names = names
        self.bounds = self.getBounds()

    def getBounds(self):
        lowX1 = min(self.x_t[:,1])
        lowX2 = min(self.x_t[:,5])
        lowX3 = min(self.x_t[:,9])
        highX1 = max(self.x_t[:,1])
        highX2 = max(self.x_t[:,5])
        highX3 = max(self.x_t[:,9])

        lowY1 = min(self.x_t[:,2])
        lowY2 = min(self.x_t[:,6])
        lowY3 = min(self.x_t[:,10])
        highY1 = max(self.x_t[:,2])
        highY2 = max(self.x_t[:,6])
        highY3 = max(self.x_t[:,10])

        return [min(lowX1, lowX2, lowX3), max(highX1,highX2, highX3), min(lowY1, lowY2, lowY3), max(highY1,highY2, highY3)]


    def plotSingleFrame(self, x):
        fig = plt.figure()

        plt.scatter(x[1],x[2], color = 'red')
        plt.scatter(x[5], x[6], color = 'blue')
        plt.scatter(x[9], x[10], color = 'g')

        titleString = f"Time: {x[0]}"
        plt.title(titleString)
        plt.legend()

        plt.show()