# basic plot 
import matplotlib.pyplot as plt
import numpy as np
import math

'''
X = np.arange(0, math.pi*2, 0.05)
y = np.sin(X)
plt.plot(X,y)
plt.xlabel("angle")
plt.ylabel("sinus")
plt.title("Angle of Sinus")
plt.show()
'''

'''
X = np.arange(0, math.pi*2, 0.05)
y = np.sin(X)
figure = plt.figure()
ax = figure.add_axes([0,0,1,1])
ax.plot(X, y)
ax.set_xlabel("Wave")
ax.set_ylabel("Sin")
ax.set_title("Wave of Sin")
plt.show()
'''

'''
plt.plot([1,2,3])
plt.show()
'''

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(222, facecolor='yellow')
ax2.plot([1,2,3])
plt.show()








