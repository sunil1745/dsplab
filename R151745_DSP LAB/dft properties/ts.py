import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
def dft(x):
	N=len(x)
	y=[]
	for k in range(0,N,1):
		sum=0
		for n in range(0,N,1):
			sum=sum+x[n]*np.exp((-j*(2*np.pi)*n*k)/N)
		y.append(sum)
	return y
#program to perform time shifting property
x=np.array(input('enter the sequence:'))
m=input('enter delay:')
m=-m
N=len(x)
n0=m%N
X=[]
y=[]
for i in range(n0,N):
	y=np.append(y,x[i])
for a in range(0,n0):
	y=np.append(y,x[a])
print y,'is x[n-n0]'
#program to find dft for shifted signal
def dft1(x,n0):
	N=len(x)
	y=[]
	for k in range(0,N,1):
		sum=0
		for n in range(0,N,1):
			sum=sum+x[n]*np.exp((-j*(2*np.pi)*n*k)/N)
		sum=sum*(np.exp((-j*2*np.pi*n0*k)/N))
		y.append(sum)
	return y
Y=dft(y)
Y1=dft1(x,n0)
plt.subplot(121)
plt.stem(Y)
plt.subplot(122)
plt.stem(Y1)
plt.show()
print Y
print Y1
