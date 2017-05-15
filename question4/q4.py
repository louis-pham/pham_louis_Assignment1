import numpy as np
import scipy.ndimage
from scipy.misc import imread
from matplotlib import pyplot as plt
from colorsys import hls_to_rgb

def zFunc(i,x,iy):
	if i==0:
		return 0 * x
	else:	
		c = x + iy
		return zFunc(i-1,x,iy)**2 + c

def setColour(z, x, iy, col):
	colArr = z.copy()
	colArr[np.abs(x + iy) <= np.abs(colArr)**2] = col
	colArr[np.abs(x + iy) > np.abs(colArr)**2] = 255 - col
	return colArr.astype(float)

lowerBound = -2
upperBound = 2
nSteps = 1000
x = np.linspace(lowerBound,upperBound,nSteps)
iy = x * 1j

xv, iyv = np.meshgrid(x,iy)

iterCol = np.array([255,255,255,255,255,255,255,255,255,255,255,255])
imgArray = []

for i, col in np.ndenumerate(iterCol):
	_z = zFunc(i[0], xv, iyv)
	imgArray.append(setColour(_z, xv, iyv, col))

plt.figure()
plt.imshow(imgArray[3], cmap='Greys', extent=[lowerBound,upperBound,lowerBound,upperBound])
plt.colorbar()
plt.figure()
plt.imshow(imgArray[10], cmap='Greys', extent=[lowerBound,upperBound,lowerBound,upperBound])
plt.colorbar()
plt.show()
