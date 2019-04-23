import numpy as np
import math
import matplotlib.pyplot as plt
m=input("enter m value:")
k=np.linspace(0,m-1,5000)
p=m-1
s=abs(k-(p/2))
y=1-((2*s)/p)
print y
plt.plot(k,y)
plt.show()
