import os

TESTDIR = 'testdir'

try:
	home = os.path.expanduser(~)
	print home

	if not os.path.exists(os.path.join(home,TESTDIR)):
		os.makedirs(os.path.join(home,TESTDIR))
		pass


except Exception, e:
	