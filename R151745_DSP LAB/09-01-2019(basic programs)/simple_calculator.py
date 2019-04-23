import math
print("\t  \t")
print("\t Simple Calculator \t")

def sum(a,b):
	a+=b
	return a

def sub(a,b):
	if a>b:
		a-=b
		return a
	else:
		b-=a
		return b
def mul(a,b):
	a*=b
	return a
def div(a,b):
	q=a/b
	r=a%b
	print("\n quotient=%s"%q)
	print("\n remainder=%s"%r)
def sqr(a):
	x=math.sqrt(a)
	return x
while(True):
	print("\n\n choose your operation:")
	print("\n\t1.addition")
	print("\n\t2.subtraction")
	print("\n\t3.multiplication")
	print("\n\t4.division")
	print("\n\t5.sqare root")
	print("\n\t6.exit")

	choice=int(input('>'))

	if choice== 1:
		print("\nenter two numbers:")
		num1=int(input('>'))
		num2=int(input('>'))
		s=sum(num1,num2)
		print("sum is:%s"%s)

	elif choice==2:
		print("\n\n enter two numbers:")
		num1=int(input('>'))
		num2=int(input('>'))
		d=sub(num1,num2)
		print("differnce is:%s"%d)

	elif choice==3:
		print("\n\nenter two numbers:")
		num1=int(input('>'))
		num2=int(input('>'))
		p=mul(num1,num2)
		print("product is:%s"%p)

	elif choice==4:
		print("\n\nenter two numbers:")
		num1=int(input('>'))
		num2=int(input('>'))
		q=div(num1,num2)

	elif choice==5:
		print("\n\nenter any number:")
		num1=int(input('>'))
		r=math.sqrt(num1)
		print("sqare root is:%s"%r)

	else:
		print("\nExit")
		print("\nprocessing...")
		print("\ncompleted")
		break
