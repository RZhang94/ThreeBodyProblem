import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
from time import sleep as sleep
from collections import deque



class animator:
    def __init__(self, x_t, names):
        self.x_t = x_t
        self.createSettings(names)
        self.createHistory()

    class settings:
        def __init__(self, names=None, animationDelay=1000/60, drawBounds=None, marginSize = 1.2, stepFrame = 1):
            self.names = names
            self.animationDelay = animationDelay
            self.drawBounds = drawBounds
            self.marginSize = marginSize
            self.stepFrame=stepFrame

    def createSettings(self, names):
        drawBounds = self.getBounds(0)
        self.settings = self.settings(names = names, drawBounds=drawBounds)

    def getBounds(self,i):
        x = [self.x_t[i,1], self.x_t[i,5],self.x_t[i,9]]
        y = [self.x_t[i,2],self.x_t[i,6],self.x_t[i,10]]

        return [min(x), max(x), min(y), max(y)]

    def createHistory(self,points=300):
        self.settings.size = self.x_t.shape
        self.settings.historyPoints = points
        self.history = np.zeros(shape = (self.settings.historyPoints, self.settings.size[1]))
        self.historyIndex = None

    def createAnimation(self):
        self.fig = plt.figure(figsize=(8,8))

        xlimits = (self.settings.drawBounds[0], self.settings.drawBounds[1])
        ylimits = (self.settings.drawBounds[2], self.settings.drawBounds[3])
        self.getBounds(0)
        ax = self.fig.add_subplot(autoscale_on=True, xlim = xlimits, ylim = ylimits)
        ax.set_aspect('equal')
        ax.grid()
        ax.set_title('Three Body Problem')


        line1, = ax.plot([],[], 'o-', lw=3, color= 'red', label = self.settings.names[0])
        line2, = ax.plot([],[],'o-', lw=3, color= 'green', label = self.settings.names[1])
        line3, = ax.plot([],[],'o-', lw=3, color= 'blue', label = self.settings.names[2])

        trace1, = ax.plot([],[], lw=1, color= 'red')
        trace2, = ax.plot([],[], lw=1, color= 'green')
        trace3, = ax.plot([],[], lw=1, color= 'blue')

        history = deque(maxlen=self.settings.historyPoints)
        time_text = ax.text(0.5, 0.9, '', transform=ax.transAxes)
        ax.legend()

        def animate(i):
            step = int(i *self.settings.stepFrame)
            def con(i,c):
                returnList = [self.x_t[i,c], self.x_t[i,c]-1]
                return returnList
            def historyExtract(trace, cs):
                c1,c2 = cs[0], cs[1]
                xData = []
                yData =[]
                for entry in history:
                    xData.append(entry[c1])
                    yData.append(entry[c2])
                trace.set_data(xData, yData)
            def getHistoryBounds():
                minX = 0
                maxX = 0
                minY = 0
                maxY = 0
                for entry in history:
                    if entry[1] > maxX:
                        maxX = entry[1]
                    if entry[5] > maxX:
                        maxX = entry[5]
                    if entry[9] > maxX:
                        maxX = entry[9]
                    if entry[1] < minX:
                        minX = entry[1]
                    if entry[5] < minX:
                        minX = entry[5]
                    if entry[9] < minX:
                        minX = entry[9]

                    if entry[2] > maxY:
                        maxY = entry[2]
                    if entry[6] > maxY:
                        maxY = entry[6]
                    if entry[10] > maxY:
                        maxY = entry[10]
                    if entry[2] < minY:
                        minY = entry[2]
                    if entry[6] < minY:
                        minY = entry[6]
                    if entry[10] < minY:
                        minY = entry[10]
                return [minX, maxX, minY, maxY]

            if i==0:
                history.clear()
            if i%2 != 0:
                history.appendleft(self.x_t[step,:])
            line1.set_data(con(step,1), con(step,2))
            line2.set_data(con(step,5), con(step,6))
            line3.set_data(con(step,9), con(step,10))

            historyExtract(trace1, [1,2])
            historyExtract(trace2, [5,6])
            historyExtract(trace3, [9,10])

            time_text.set_text(f'Simulation Time {self.x_t[step,0]}')

            pointBounds = self.getBounds(step)
            historyBounds = getHistoryBounds()
            bounds = [min(historyBounds[0],pointBounds[0]),max(historyBounds[1],pointBounds[1]),min(historyBounds[2],pointBounds[2]),max(historyBounds[3],pointBounds[3]) ]
            xlimits = (bounds[0], bounds[1])
            ylimits = (bounds[2], bounds[3])
            xdist = xlimits[1]-xlimits[0]
            ydist = ylimits[1]-ylimits[0]
            xmid = xlimits[1]-xdist/2
            ymid = ylimits[1]-ydist/2
            newxlimits = (xmid-xdist/2*self.settings.marginSize, xmid+xdist/2*self.settings.marginSize)
            newylimits = (ymid-ydist/2*self.settings.marginSize, ymid+ydist/2*self.settings.marginSize)
            ax.set_xlim(newxlimits)
            ax.set_ylim(newylimits)
            return line1, line2, line3, trace1, trace2, trace3, time_text,

        animation = ani.FuncAnimation(fig= self.fig, func= animate, frames= int(self.settings.size[0]/self.settings.stepFrame)-1, interval=self.settings.animationDelay)
        plt.show()
