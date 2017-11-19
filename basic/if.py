age = 20
if age < 30:
		print 'i am ,' , age
		print 'adult'


names = ['michale','bob','trance']

for name in names:
	print name
	pass

sum = 0

for x in xrange(0,101):
	sum = sum + x
	pass
print sum

while sum > 0:
	sum = sum - 2
	pass

print 'i learning python'

birth = int(raw_input('your birth :'))

if birth > 2000:
	print '00'
	pass


d = {"wangchao" : 26,"julia" : 27}

print d

d["wangchao"] = 29

print d

s = set([1,2,3,4,5])
s1 = set([2,3,4,5,6,7,8])

print s & s1



