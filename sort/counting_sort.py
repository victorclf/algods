import random


def countingSort0tok(l, k, key=lambda x: x):
    """
    Sorts l in O(nk) time using the counting sort algorithm. keys in l must be in the interval [0, k].

    :param l: list to sort
    :param k: keys are in range 0 to k
    :param key: function for returning key of the element
    :return: new sorted list
    """

    # Count occurrences
    c = [0] * (k + 1)
    for e in l:
        c[key(e)] += 1

    # Transform count array into prefix sum
    for i in range(1, k + 1):
        c[i] += c[i - 1]

    r = [0] * len(l)
    # Build sorted array
    for e in reversed(l):
        r[c[key(e)] - 1] = e
        c[key(e)] -= 1

    return r


def countingSort(l, maxKey, minKey=0, key=lambda x: x):
    """
    Sorts l in O(nk) time using the counting sort algorithm. keys in l must be in the interval [minKey, maxKey].

    :param l: list to sort
    :param maxKey: keys are in range [minKey, maxKey]
    :param minKey: keys are in range [minKey, maxKey]
    :param key: function for returning key of the element
    :return: new sorted list
    """

    _key = key if minKey == 0 else (lambda x: key(x) - minKey)
    maxKey = maxKey - minKey
    return countingSort0tok(l, maxKey, _key)


if __name__ == '__main__':
    minKey = -2000
    maxKey = 1000
    base = [random.randrange(minKey, maxKey) for i in range(1000)]

    expected = base.copy()
    expected.sort()

    l = countingSort(base, maxKey, minKey=minKey)

    print(l)
    print(expected)
    assert l == expected
