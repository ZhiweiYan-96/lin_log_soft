from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

def logistic(z):
	return 1/(1+np.exp(-z))

#Plot the logistic function 
z=np.linspace(-6,6,100)
plt.plot(z,logistic(z),'b-')
plt.xlabel('$z$',fontsize=15)
plt.ylabel('$\sigma(z)$',fontsize=15)
plt.title('logistic function')
plt.grid()
plt.show()

def logistic_derivative(z):
	return logistic(z)*(1-logistic(z))

z=np.linspace(-6,6,100)
plt.plot(z,logistic_derivative(z),'r-')
plt.xlabel('$z$',fontsize=15)
plt.ylabel('$\\frac{\\partial \\sigma(z)}{\\partial z}$', fontsize=15)
plt.title('derivatvie of the logistic function')
plt.grid()
plt.show()