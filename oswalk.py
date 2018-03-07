import os

path = '/Users/edz/Desktop/FLTv-iOS'
for root, dirs, files in os.walk(path, True):
    print ('root: %s' % root)
    print ('dirs: %s' % dirs)
    print ('files: %s' % files)
    print ('')
