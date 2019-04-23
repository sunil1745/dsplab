import numpy as np
import matplotlib.pyplot as plt
a=input("enter 1st sequence:")
b=input("enter 2nd sequence:")
lengtha=len(a)
lengthb=len(b)
c=np.zeros(lengtha+lengthb-1)
for m in range(lengtha):
		for n in range(lengthb):
			c[m+n]=c[m+n]+a[m]*b[n]
print(c)
print("convolution result:")
print(np.convolve(a,b))
a1=plt.subplot(311)
plt.stem(a)
plt.subplot(312,sharex=a1,sharey=a1)
plt.stem(b)
plt.subplot(313,sharex=a1,sharey=a1)
plt.stem(c)
plt.show()
