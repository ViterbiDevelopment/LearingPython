import math

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x


z = my_abs(100)

print z

def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx , ny

r = move(100,100,60,math.pi / 6)

print r

def power(x,n = 1):
	s = 1
	while  n > 0:
		n = n -1
		s = s * x
	return s

print power(5)

def  calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print calc([1,2,3,4])

haha = {'city': 'Beijing', 'job': 'Engineer'}
def person(name,age,**kw):
	print 'name :',name,'age:',age,'other',kw

print person('wangchao',25,**haha)




