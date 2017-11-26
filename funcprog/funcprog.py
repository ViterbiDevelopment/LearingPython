def f(x):
	return x * x
print map(f,[1,2,3,4,5,6])

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print char2num('8')

def prod(t):
    return reduce(lambda x,y:x*y,t)
t=[1,2,3]
print prod(t)


def fn(x,y):
	return x*10 + y
print reduce(fn,[1,3,5,7,9])

print reduce(fn,map(char2num,'13579'))

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([1,2,3,4,5],reversed_cmp)

def count():
	fs = []
	for x in xrange(1,4):
		def f():
			return x * x
		fs.append(f)
	return fs

print count()

f1,f2,f3 = count()

print f1()


def now():
	print "2017 - 11 - 22"
f = now
f()
print f.__name__

// 装饰器 还是挺难理解的

def test1():
	pass
def test1():
	pass



