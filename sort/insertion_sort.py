import random


def insertionSort(l, key=lambda x: x):
    for i in range(1, len(l)):
        e = l[i]
        j = i - 1
        while j >= 0 and l[j] > key(e):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = e


if __name__ == '__main__':
    base = [random.randrange(100_000) for i in range(1000)]

    expected = base.copy()
    expected.sort()

    l = base.copy()
    insertionSort(l)

    print(l)
    print(expected)
    assert l == expected
