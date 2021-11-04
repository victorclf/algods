import random

from counting_sort import *


def radixSort(l, digits, radix=10):
    def getDigit(n, i):
        return (n // radix ** i) % radix

    for i in range(digits):
        l = countingSort0tok(l, radix - 1, key=lambda x: getDigit(x, i))

    return l


if __name__ == '__main__':
    digits = 6
    n = 10_000
    base = [random.randrange(10 ** (digits - 1), 10 ** digits) for i in range(n)]

    expected = base.copy()
    expected.sort()

    l = radixSort(base, digits)
    l2 = radixSort(base, digits, radix=256)

    print(l)
    print(l2)
    print(expected)
    assert l == expected
    assert l2 == expected