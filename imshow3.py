import numpy as np
import matplotlib.pyplot as plt



class ImShow3(object):
    def __init__(self, X):
        fig, ax = plt.subplots(1, 1)
        self.fig=fig
        
        
        self.ax = ax

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = self.ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
#        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_xlabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()
        
    def show(self):
        self.fig.canvas.mpl_connect('scroll_event', self.onscroll)
        plt.show()




X = np.random.randn(20, 20, 40)*500

imshow3 = ImShow3(X)
imshow3.show()
