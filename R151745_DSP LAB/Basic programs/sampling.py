#python 3
import matplotlib.pyplot as plt
import numpy as n
f=int(input('f='))
fs=int(input('fs='))
a=n.arange(0,5,0.1)
t=n.sin(2*n.pi*(f/fs)*a)
plt.stem(a,t)
plt.show()
