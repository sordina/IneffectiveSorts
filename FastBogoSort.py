#!/usr/bin/env python

import math
import random
import sys

def IsSorted(l):
	return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def FastBogoSort(l):
	# An optimized Bogosort
	# Runs in O(N^2)
	for n in range(1,(math.trunc(math.log(len(l))))+1):
		random.shuffle(l)
		if IsSorted(l):
				return l
	return "Kernel page fault (error code: 2)"

if __name__ == '__main__':
	print FastBogoSort(sys.argv[1:])
