#!/usr/bin/env python3

import collections

'''
Maximum Subarray Problem

IN: 
	An array A of numbers
OUT:
	A contiguous subarray of A with the largest possible sum represented
	by the tuple (sum, startIndex, endIndex), where endIndex is exclusive.

References:
- CLRS 3rd ed. - Chapter 4
- https://en.wikipedia.org/wiki/Maximum_subarray_problem
'''

MaximumSubarray = collections.namedtuple('MaximumSubarray', 'sum start end')

'''
Kadane's algorithm.

This version does not accept the empty subarray as valid.

Running time: O(n)
'''
def maximumSubarray(array):
	bestSum = None
	bestStart = None
	bestEnd = None
	currentSum = None
	currentStart = None
	currentEnd = None
	
	for index, number in enumerate(array):
		if currentSum is None or currentSum < 0:
			currentSum = number
			currentStart = index
			currentEnd = index + 1
		else:
			currentSum += number
			currentEnd += 1
		
		if bestSum is None or currentSum > bestSum:
			bestSum = currentSum
			bestStart = currentStart
			bestEnd = currentEnd
		
	return MaximumSubarray(sum=bestSum, start=bestStart, end=bestEnd)
	
	
if __name__ == '__main__':
	r1 = maximumSubarray([20, -25, 5, 5, 19])
	assert r1.sum == 29
	assert r1.start == 2
	assert r1.end == 5
	
	r2 = maximumSubarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
	assert r2.sum == 43
	assert r2.start == 7
	assert r2.end == 11
	
	r3 = maximumSubarray([])
	assert r3.sum is None
	assert r3.start is None
	assert r3.end is None
	
	r4 = maximumSubarray([-1, -4, -5])
	assert r4.sum == -1
	assert r4.start == 0
	assert r4.end == 1
	
	r5 = maximumSubarray([4, 3, 3])
	assert r5.sum == 10
	assert r5.start == 0
	assert r5.end == 3
	
	# Prefer largest subarray even though sum is the same, i.e. [5, -5, 10] instead of [10] here
	r6 = maximumSubarray([5, -5, 10])
	assert r6.sum == 10
	assert r6.start == 0
	assert r6.end == 3
