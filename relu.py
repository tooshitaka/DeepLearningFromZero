import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)

x = np.arange(-6, 6, 0.01)
y = relu(x)
plt.plot(x,y)
plt.ylim(-1,6)
plt.show()
