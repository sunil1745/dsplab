#python 3
import matplotlib.pyplot as plt
import numpy as n
f=0.5
a=n.arange(0,3,0.01)
t=n.sin(2*n.pi*f*a)
f1=1
b=n.arange(0,3,0.01)
t1=n.sin(2*n.pi*f1*b)
x=t+t1
c=n.arange(0,3,0.01)
plt.plot(a,t)
plt.show()
plt.plot(b,t1)
plt.show()
plt.plot(c,x)
plt.show()

