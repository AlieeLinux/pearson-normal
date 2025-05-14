import pandas as pd
import numpy as np
from math import pow, sqrt
import matplotlib.pyplot as plt

class Function:
    def __init__(self, x, y, length : int):
        self.xsq = np.empty(length)
        self.ysq = np.empty(length)
        self.xsq = x
        self.ysq = y

    @staticmethod
    def Calculate(x, y, xsq, ysq, xy, length):
        top = length*xy - x*y
        down = ((length*xsq) - (pow(x, 2))) * (length * ysq - pow(y, 2))
        down = sqrt(down)
        answer = top/down
        return float(answer)



    def frame(self):
        xsqu = np.empty(len(self.xsq))
        ysqu = np.empty(len(self.xsq))
        xy = np.empty(len(self.xsq))
        for s in range(len(xsqu)):
            xy[s] = self.xsq[s] * self.ysq[s]
            xsqu[s] = pow(self.xsq[s], 2)
            ysqu[s] = pow(self.ysq[s], 2)

        xyTotal = np.sum(xy)
        ysquTotal = np.sum(ysqu)
        xsquTotal = np.sum(xsqu)
        xtotal = np.sum(self.xsq)
        yTotal = np.sum(self.ysq)

        s = Function.Calculate(xtotal, yTotal, xsquTotal, ysquTotal, xyTotal, len(xy))

        print("r=", s)

        Function.Correlation(s)


        i = pd.DataFrame({
            "x" : self.xsq,
            "y" : self.ysq,
            "xy" : xy,
            "xpow2" : xsqu,
            "ypow2" : ysqu
        })
        print(i)
        return 0

    @staticmethod
    def Correlation(r : float):
        if r == 1.0:
            print("Perfect positive correlation")
        elif 0.69 < r <= 0.99999:
            print("Strong positive correlation")
        elif 0.000001 < r <= 0.68:
            print("moderate positive")
        elif r == 0:
            print("no correlation")

    def Graphh(self):
        i = np.empty(len(self.xsq))
        num = 1
        for a in range(len(i)):
            i[a] = num
            num=num+1

        plt.scatter(i, self.ysq)
        plt.scatter(i, self.xsq)
        plt.plot(i, self.xsq)
        plt.plot(i, self.ysq)
        plt.savefig("viewme.png")


