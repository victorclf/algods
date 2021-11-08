import random


def _setRandomPivot(l, a, b):
    randomIndex = random.randrange(a, b)
    lastIndex = b - 1
    l[lastIndex], l[randomIndex] = l[randomIndex], l[lastIndex]
    return l[lastIndex]


def _partition(l, a, b):
    pivot = _setRandomPivot(l, a, b)

    i = a  # [a, i) will holds elements less or equal pivot and [i, j + 1) the ones greater than pivot
    for j in range(a, b - 1):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[b - 1], l[i] = l[i], l[b - 1]  # move pivot to middle of two lists (the <= list and the > list)
    return i


def _quickselect(l, a, b, k):
    subListLength = b - a
    if subListLength <= 1:
        return l[a]

    pivotIndex = _partition(l, a, b)
    q = pivotIndex - a  # l[pivotIndex] is the q-th smallest number of the sublist l[a:b]
    if k == q:
        return l[pivotIndex]
    if k < q:
        return _quickselect(l, a, pivotIndex, k)
    else:
        return _quickselect(l, pivotIndex + 1, b, k - q - 1)


def quickselect(l, k):
    """
    Finds the (k + 1)-th smallest element in list l in linear time using the randomized quickselect algorithm.
    :param l: list to search
    :param k: index k indicating the (k + 1)-th smallest element to look for
    :return: the (k + 1)-th smallest element
    :raise: IndexError if 0 <= k < len(l)
    """
    if not (0 <= k < len(l)):
        raise IndexError()
    return _quickselect(l, 0, len(l), k)


if __name__ == '__main__':
    n = 1000
    l = list(range(n))

    for k in range(n):
        random.shuffle(l)
        index = quickselect(l, k)
        print(l)
        print(f'k: {k}')
        print(f'l[{index}]: {l[index]}')
        assert l[index] == k