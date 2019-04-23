import numpy as np
import cmath as cm
import matplotlib.pyplot as plt
n=np.linspace(-100,100,100)
w=np.pi/4
y=[]
y1=(np.sin(w*n))/(n*np.pi)
y=np.append(y,y1)
j=cm.sqrt(-1)
def dtft(x):
	N=len(x)
	X=[]
	W=np.linspace(-np.pi,np.pi,100)
	for i in range(0,100):
		sum=0
		for n in range(0,N,1):
			sum=sum+x[n]*np.exp(-j*W[i]*n)
	
		X.append(sum)
	return X
Y=dtft(y)
plt.subplot(2,1,1)
plt.stem(n,y1)
plt.subplot(2,1,2)
plt.stem(np.abs(Y))
plt.show()
