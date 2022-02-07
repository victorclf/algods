import util


def nextPermutation(l):
    """Transform l into next permutation in lexicographic order."""

    # Find the largest index k such that a[k] < a[k + 1]
    k = None
    for i in range(len(l) - 1, 0, -1):
        if l[i - 1] < l[i]:
            k = i - 1
            break

    # If no such index k exists, the permutation is the last permutation and the list is sorted  in decreasing order.
    if k is None:
        l.reverse()
        return l

    # Find the largest index l greater than k such that a[k] < a[l].
    for i in range(len(l) - 1, k, -1):
        if l[k] < l[i]:
            l[k], l[i] = l[i], l[k]  # swap the value of a[k] with that of a[l].
            util.reverseSublist(l, start=k + 1)  # reverse the sequence from a[k + 1] to and a[n] (inclusive interval)
            break


if __name__ == '__main__':
    a = []
    nextPermutation(a)
    assert a == []
    a = [1]
    nextPermutation(a)
    assert a == [1]
    a = [1, 2, 3]
    nextPermutation(a)
    assert a == [1, 3, 2]
    nextPermutation(a)
    assert a == [2, 1, 3]
    nextPermutation(a)
    assert a == [2, 3, 1]
    nextPermutation(a)
    assert a == [3, 1, 2]
    nextPermutation(a)
    assert a == [3, 2, 1]
    nextPermutation(a)
    assert a == [1, 2, 3]

    a = list(range(-2, 2))
    before = []
    for i in range(23):
        before.append(a.copy())
        nextPermutation(a)
        assert a not in before
        assert len(a) == len(before[-1])
        assert all([(x in before[-1]) for x in a])
    nextPermutation(a)
    assert a == sorted(a)


