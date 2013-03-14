#!/usr/bin/env python

# Am I allowed to use the standard libraries?
import math
import sys

def IsSorted(l):
	return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def ChoosePivot(l):
	return l[math.trunc(len(l) / 2)]

def DivideList(l):
	p = math.trunc(len(l) / 2)
	return [l[:p], l[p:]]

def JobInterviewQuickSort(l):
	# OK so you choose a pivot
	pivot  = ChoosePivot(l)
	# Then divide the list in half
	halves = DivideList(l)
	# For each half
	for h in halves:
		# Check to see if it's sorted
		if IsSorted(h):
			# No, wait, it doesn't matter
			None
		newList = []
		# Compare each element to the pivot
		for e in h:
			if e > pivot:
				# The bigger ones go in a new list
				newList.append(e)
			elif e == pivot:
				# The equal ones go into, uh
				# the second list from before
				halves[1].append(e)
		"""
		# Hang on, let me name the lists
		# This is list a
		a = h
		# The new one is list b
		b = newList
		# Put the big ones into list B
		...
		# Now take the second list
			# Call it list, uh, a2
		a2 = halves[1]
		# Which one was the pivot in?
		# Scratch all that
		"""
		# It just recursively calls itself
		# until both lists are empty
			# Right?
		"""
		while halves[0] or halves[1]:
			JobInterviewQuickSort(h)
		# Not empty, but you know what I mean
		"""
		# I know what you mean
		while halves[0][1:] or halves[1][1:]:
			JobInterviewQuickSort(h)

if __name__ == '__main__':
	print JobInterviewQuickSort(sys.argv[1:])
