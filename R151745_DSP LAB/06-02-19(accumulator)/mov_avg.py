import numpy as np
import matplotlib as matplotlib  # for plotting
import matplotlib.pyplot as plt
np.random.seed(17)
n=10
N = 500
x = np.linspace(0, n, N)
y0 = -0.05*x**4 + 5*x**2 + 7*x - 6
yn = 4.5*np.random.standard_normal(N) * np.log10(y0**2 + 0.1)/2
y = y0 + yn 
#code2:
def running_mean(l, N):
        sum = 0
        result = list( 0 for x in l)
     
        for i in range( 0, N ):
            sum = sum + l[i]
            result[i] = sum / (i+1)
     
        for i in range( N, len(l) ):
            sum = sum - l[i-N] + l[i]
            result[i] = sum / N
     
        return result
