#!/usr/bin/env python

import math
import sys

def HalfHeartedMergeSort(l):
	if len(l) < 2:
		return l
	pivot = math.trunc(len(l)/2)
	a = HalfHeartedMergeSort(l[:pivot])
	b = HalfHeartedMergeSort(l[pivot:])
	# UMMMMM
	return [a,b] # Here. Sorry.

if __name__ == '__main__':
	print HalfHeartedMergeSort(sys.argv[1:])
