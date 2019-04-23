import numpy as np
import cmath as cm
import matplotlib.pyplot as plt
e=input("enter e/m value:")
k=np.linspace(0,e-1,5000)
p=e-1
s=abs(k-(p/2))
f=1-((2*s)/p)
print f#WINDOW
n=np.linspace(-100,100,100)
n1=np.linspace(0,e-1,100)
w=np.pi/4
y=[]
y5=[]
y1=(np.sin(w*n))/(n*np.pi)#non casual signal
y4=(np.sin(w*n1))/(n1*np.pi)#casual signal
y=np.append(y,y1)
y5=np.append(y5,y4)
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
Y=dtft(y)#dtft of sinc pulse
F=dtft(f)#dtft of triangular window
b=[]
b1=[]
for j in range(1,e):
	q=y[j]*f[j]
	b1=np.append(b1,q) 
b1=np.linspace(1,e-1,5000)
B1=dtft(b1)
plt.subplot(3,2,1)
plt.stem(n,y1)#sinc function
plt.subplot(3,2,2)
plt.plot(np.abs(Y))#dtft of sinc function
plt.subplot(3,2,3)
plt.plot(k,f)#triangular window
plt.subplot(3,2,4)
plt.stem(n1,y5)#casual signal plot
plt.subplot(3,2,5)
plt.plot(k,b1)#product of casual signal and triangular window
plt.subplot(3,2,6)
plt.plot(np.abs(B1))#dtft of product 
plt.show()
