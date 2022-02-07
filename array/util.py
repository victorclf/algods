def reverseSublist(l, start=0, end=None):
    """ Reverse sublist in place. """
    if end is None:
        end = len(l)
    for x in range(0, (end - start) // 2):
        l[start + x], l[end - x - 1] = l[end - x - 1], l[start + x]


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5]
    reverseSublist(a)
    assert a == [5, 4, 3, 2, 1, 0]
    a = [0, 1, 2, 3, 4, 5]
    reverseSublist(a, start=2)
    assert a == [0, 1, 5, 4, 3, 2]
    a = [0, 1, 2, 3, 4, 5]
    reverseSublist(a, start=3, end=4)
    assert a == [0, 1, 2, 3, 4, 5]
    a = [0, 1, 2, 3, 4, 5]
    reverseSublist(a, start=3, end=5)
    assert a == [0, 1, 2, 4, 3, 5]