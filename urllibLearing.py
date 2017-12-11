# urlLib learing

import urllib2
import urllib

response = urllib2.urlopen('http://blog.csdn.net/pleasecallmewhy/article/details/8923067')
html = response.read()
print html