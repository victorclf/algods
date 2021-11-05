import random
from insertion_sort import *


def bucketSortUniform(l):
    n = len(l)
    buckets = [[] for i in range(n)]

    for e in l:
        buckets[int(e * n)].append(e)

    i = 0
    for b in buckets:
        for e in b:
            l[i] = e
            i += 1

    insertionSort(l)

    return l


if __name__ == '__main__':
    n = 10_000
    base = [random.random() for i in range(n)]

    expected = base.copy()
    expected.sort()

    l = bucketSortUniform(base)

    print(l)
    print(expected)
    assert l == expected