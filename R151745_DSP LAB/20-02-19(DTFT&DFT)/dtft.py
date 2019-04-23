#R151745
import numpy as np
import cmath as cm
import matplotlib.pyplot as plt
j=cm.sqrt(-1)
def dtft(x):
	N=len(x)
	X=[]
	W=np.linspace(0,2*np.pi,10000)
	for i in range(0,10000):
		sum=0
		for n in range(0,N,1):
			sum=sum+x[n]*np.exp(-j*W[i]*n)
	
		X.append(sum)
	return X
x=np.array(input('enter the sequence='))
y=dtft(x)
print dtft(x)
plt.subplot(2,1,1)
plt.plot(np.abs(y))
plt.subplot(2,1,2)
plt.plot(np.angle(y))
plt.show()                                                                             
