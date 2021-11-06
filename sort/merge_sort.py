import random


def merge(l, a, mid, b):
    left = l[a:mid] + [float('inf')]
    right = l[mid:b] + [float('inf')]

    leftIndex = 0
    rightIndex = 0
    for i in range(a, b):
        if left[leftIndex] <= right[rightIndex]:
            l[i] = left[leftIndex]
            leftIndex += 1
        else:
            l[i] = right[rightIndex]
            rightIndex += 1


def ms(l, a, b):
    if (a + 1) < b:
        mid = (a + b) // 2
        ms(l, a, mid)
        ms(l, mid, b)
        merge(l, a, mid, b)


def mergeSort(l):
    return ms(l, 0, len(l))


if __name__ == '__main__':
    base = [random.randrange(-1_000, 1_000) for i in range(10_000)]

    expected = base.copy()
    expected.sort()

    l = base.copy()
    mergeSort(l)

    print(l)
    print(expected)
    assert l == expected
