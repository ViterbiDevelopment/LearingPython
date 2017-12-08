#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(raw_input('x'))
y = int(raw_input('y'))
z = int(raw_input('z'))

l = [x,y,z]

for i in xrange(0,3):
	for j in xrange(i,3):
		if l[i] > l[j]:
			temp = l[i]
			l[i] = l[j]
			l[j] = temp
print l