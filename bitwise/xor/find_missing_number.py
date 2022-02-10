def findMissingNumber(sequence, startNumber, endNumber):
    '''
    Given a sequence [startNumber, endNumber) which is missing a single number, finds this missing single number in O(n)
     time using XOR.

    :param sequence:
    :param startNumber:
    :param endNumber:
    :return: the missing number
    '''
    wholeListXor = 0
    for i in range(startNumber, endNumber):
        wholeListXor ^= i

    sequenceXor = 0
    for i in sequence:
        sequenceXor ^= i

    missingNumber = wholeListXor ^ sequenceXor

    return missingNumber


if __name__ == '__main__':
    start1 = 341
    end1 = 1000
    missing1 = 498
    s1 = list(range(start1, missing1)) + list(range(missing1 + 1, end1))
    assert findMissingNumber(s1, start1, end1) == missing1

    start2 = -123341
    end2 = 1123190
    missing2 = -2322
    s2 = list(range(start2, missing2)) + list(range(missing2 + 1, end2))
    assert findMissingNumber(s2, start2, end2) == missing2