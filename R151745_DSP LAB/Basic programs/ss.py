
a=int(input('Enter no of rows in 1st matrix:'))
b=int(input('Enter no of columns in 1st matrix:'))
c=int(input('Enter no of rows in 2nd matrix:'))
d=int(input('Enter no of columns in 2nd matrix:'))
m=[]
for i in range(0,a,1):
	l = []
	for j in range(b):
		l.append(int(input()))
	m.append(l)
n=[]
for i in range(c):
	l = []
	for j in range(d):
		l.append(int(input()))
	n.append(l)

r = [[0 for i in range(d)] for j in range(a)]
if (b == c):
	for i in range(a):
		for j in range(d):
			for l in range(b):
				r[i][j] += m[i][l] * n[l][j]
	print(r)	
else:
	print("Matrix Mutiplication is not applicable")




