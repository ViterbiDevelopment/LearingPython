import os
L = ['Michal','Sarah','Trancy']

print L[0:3]

i = range(100)

print i[0:10]
print i[-8:]
print i[0:10:2]
print i[0::5]

m = [x*x for x in range(1,11)]
print m

n = [X + Y for X in 'ABC' for Y in 'DEF']
print n

#d = [d in os.listdir('.')]
print [d for d in os.listdir('.')]

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
    	yield 'a,b',(a,b)
        a, b = b , a + b
        n = n + 1
print fib(10)

for n in fib(6):
	print n