from heap.min_heap import MinHeap


def heapsort(iterable):
    h = MinHeap(list(iterable))
    return [h.remove(0) for i in range(len(h))]


# Using the heapq library: https://docs.python.org/3/library/heapq.html
def heapq_heapsort(iterable):
    from heapq import heapify, heappop
    h = list(iterable)
    heapify(h)
    return [heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    l1 = [4, -1, 10, 1, 2, 6, -4, -1, 0, 2, 2, 0, 3, 5, 7, 3, 19, 17]
    l2 = [2]
    l3 = []
    assert heapsort(l1) == list(sorted(l1))
    assert heapsort(l2) == list(sorted(l2))
    assert heapsort(l3) == list(sorted(l3))






