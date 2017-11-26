import functools

# 
# def log(func):
#	def wrapper(*args,**kw):
#		print 'call %s():' % func.__name__
 #       return func(*args, **kw) 

#@log
#def  now():
#	print '2017-11-26'

#now()

int2 = functools.partial(int , base = 2)

print int2('10000000000')
