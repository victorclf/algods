import random


def getMedianOf3Index(l, a, b):
    firstIndex = a
    midIndex = (a + b) // 2
    lastIndex = b - 1
    first = l[firstIndex]
    mid = l[midIndex]
    last = l[lastIndex]
    if first <= mid:
        if mid <= last:
            return midIndex  #first <= mid <= last
        else:
            if first <= last:
                return lastIndex  # first <= last <= mid
            else:
                return firstIndex  # last < first <= mid
    else: # first > mid
        if first <= last:
            return firstIndex  # mid < first <= last
        else: # first > mid and first > last
            if mid <= last:
                return lastIndex # mid <= last < first
            else:
                return midIndex # last < mid < first


def moveMedianToPivotPosition(l, a, b):
    medianIndex = getMedianOf3Index(l, a, b)
    lastIndex = b - 1
    l[medianIndex], l[lastIndex] = l[lastIndex], l[medianIndex]


def partition(l, a, b):
    moveMedianToPivotPosition(l, a, b)
    lastIndex = b - 1
    pivot = l[lastIndex]
    i = j = a - 1    # [a, i + 1) will holds elements less or equal pivot and [i + 1, j + 1) the ones greater than pivot
    for j in range(a, b - 1):
        if l[j] <= pivot:
            l[i + 1], l[j] = l[j], l[i + 1]
            i += 1
    l[i + 1], l[lastIndex] = l[lastIndex], l[i + 1]  # move pivot to middle of two lists (the <= list and the > list)
    return i + 1


def qs(l, a, b):
    if b - a > 1:
        q = partition(l, a, b)
        qs(l, a, q)
        qs(l, q + 1, b)


def quicksort(l):
    qs(l, 0, len(l))


if __name__ == '__main__':
    base = [random.randrange(100_000) for i in range(10000)]

    expected = base.copy()
    expected.sort()

    l = base.copy()
    quicksort(l)

    assert l == expected
    print(l)
    print(expected)