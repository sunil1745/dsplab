#pyhton 3
import matplotlib.pyplot as plt
import numpy as np
a=int(input('Enter no of rows in 1st matrix:'))
b=int(input('Enter no of columns in 1st matrix:'))
m=[]
for i in range(a):
	l = []
	for j in range(b):
		l.append(int(input()))
	m.append(l)
print (m)
t=m
x = np.array(t) 
y = np.linalg.inv(x) 
print (x)
print (y) 
