"""
REFERENCE
http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
"""

#Matplotlib is an excellent 2D and 3D graphics
#library for generating scientific figures


#A simple figure with MATLAB-like plotting API:

from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)
y = x ** 2
"""
#pylab
#MATLAB-like plotting API 
#everything is global
#not got for complex plots...okay for only simple ones
figure()
plot(x, y, 'y')
xlabel('x')
ylabel('y')
title('title')
show()

figure()
subplot(2,2,1)
plot(x,y,'r--')
subplot(2,2,2)
plot(y, x, 'g*-');
subplot(2,2,3)
plot(y, x, 'b');
show()
"""
#matplotlib.pyplot
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('xmen')
axes.set_ylabel('ywomen')
axes.set_title('blah')
