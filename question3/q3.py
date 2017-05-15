from scipy import integrate
import numpy as np
import scipy.special
import scipy.ndimage
from scipy.misc import imread
from matplotlib import pyplot as plt
#from PIL import Image

def _integrand(theta, m, x):
	return np.cos(m * theta - x * np.sin(theta))

def Bessel(m,x):
	I, err = integrate.quad(_integrand, 0, np.pi, args=(m,x), epsabs=1e-14)
	return I / np.pi

def pointSpread(I_o, a, x, y, lamb, R):
	q = np.sqrt(x ** 2 + y ** 2)
	ex = (2 * np.pi * a * q) / (lamb * R)
	# integrate.quad doesn't play nice with numpy arrays, so explicitly loop through ex :(
	results = np.empty(ex.shape)
	for index, _ex in np.ndenumerate(ex):
		results[index] = I_o * (Bessel(1,_ex)/_ex) ** 2
	return results

if __name__ == "__main__":
	#print Bessel(3,4)
	#print scipy.special.jv(3,4)
	#x = range(0,100)
	#m1, = plt.plot(x, [Bessel(1, _x) for _x in x], label="m=1")
	#m4, = plt.plot(x, [Bessel(4, _x) for _x in x], label="m=4")
	#m9, = plt.plot(x, [Bessel(9, _x) for _x in x], label="m=9")
	#m13, = plt.plot(x, [Bessel(13, _x) for _x in x], label="m=13")
	#plt.legend([m1,m4,m9,m13], ["m=1","m=4","m=19","m=13"])
	I_o = 30
	a = 180
	lamb = 600
	R = 15
	lowerBound = -50
	upperBound = 50
	nSteps = 200
	x = np.linspace(lowerBound,upperBound,nSteps)
	y = x.copy()
	xv, yv = np.meshgrid(x,y)
	vals = pointSpread(I_o, a, xv, yv, lamb, R)

	plt.figure()
	plt.imshow(vals, cmap='gist_gray', extent=[lowerBound,upperBound,lowerBound,upperBound])
	plt.title("Point Spread Function Values")
	plt.colorbar()

	astroImageNp = imread("n218.jpg", flatten=True)
	#astroImageNp = np.array(astroImage)
	print vals.shape
	print astroImageNp.shape
	plt.figure()
	plt.imshow(astroImageNp, cmap='gist_gray')
	plt.title("Astro Image - Before PSF")
	plt.colorbar()

	astroConvolved = scipy.ndimage.filters.convolve(astroImageNp, vals)
	plt.figure()
	plt.imshow(astroConvolved, cmap='gist_gray')
	plt.title("Astro Image - After PSF")
	plt.colorbar()
	plt.show()
	
	

	

