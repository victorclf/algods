import heapq
import sys

'''
Merge k sorted linked lists

IN: 
	An array of heads of sorted linked lists
OUT:
	Head of a sorted linked list containing all elements from the input lists.

References:
- CLRS
- https://en.wikipedia.org/wiki/K-way_merge_algorithm
'''

# For the problem with regular lists, use the built-in library heapq: 
#   heapq.merge(*iterables, key=None, reverse=False)


class LinkedListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
	def __lt__(self, other):
		return self.val < other.val
		
	def __str__(self):
		s = ''
		node = self
		while node:
			s += f'{node.val} '
			node = node.next
		return s.strip()

def mergeKListsWithHeap(lists):
	"""
	Algorithm using min heap.

	Running time: O(n lgk)
	"""
	
	kHeap = [head for head in lists if head]
	heapq.heapify(kHeap)

	mergedListHead = None
	mergedListTail = None
	while kHeap:
		smallestNode = kHeap[0]

		if mergedListHead is None:
			mergedListHead = smallestNode
			mergedListTail = smallestNode
		else:
			mergedListTail.next = smallestNode
			mergedListTail = smallestNode

		if smallestNode.next:
			heapq.heapreplace(kHeap, smallestNode.next)
		else:
			heapq.heappop(kHeap)

	return mergedListHead

def mergeKListsWithMergeSort(lists):
	"""
	K-way merging using merge sort.

	Running time: O(n lgk)
	"""
	
	def merge(a, b):
		cNodeBeforeHead = LinkedListNode()
		cTail = cNodeBeforeHead

		while a and b:
			if a.val <= b.val:
				cTail.next = a
				cTail = a
				a = a.next
			else:
				cTail.next = b
				cTail = b
				b = b.next

		if a:
			cTail.next = a
		elif b:
			cTail.next = b

		return cNodeBeforeHead.next
	
	
	while len(lists) > 1:
		newLists = []
		for i in range(len(lists) // 2):
			newLists.append(merge(lists[2*i], lists[2*i + 1]))
		if not len(lists) % 2 == 0:
			newLists.append(lists[-1])
		lists = newLists
	return lists[0] if lists else []


if __name__ == '__main__':
	def generateInputLists():
		return [LinkedListNode(2, LinkedListNode(9, LinkedListNode(11))),
			LinkedListNode(-44, LinkedListNode(0, LinkedListNode(0))),
			LinkedListNode(1, LinkedListNode(56, LinkedListNode(99, LinkedListNode(99)))),
			LinkedListNode(22)]

	expectedResult = '-44 0 0 1 2 9 11 22 56 99 99'
	assert str(mergeKListsWithHeap(generateInputLists())) == expectedResult
	assert str(mergeKListsWithMergeSort(generateInputLists())) == expectedResult

