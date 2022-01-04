from xor.find_missing_number import findMissingNumber


def findDuplicateNumber(sequence, startNumber, endNumber):
    '''
    Given a sequence [startNumber, endNumber) with a single duplicate number, find this single duplicate number in O(n)
     time using XOR.

    :param sequence:
    :param startNumber:
    :param endNumber:
    :return: the duplicate number
    '''
    return findMissingNumber(sequence, startNumber, endNumber)


if __name__ == '__main__':
    start1 = 341
    end1 = 1000
    duplicate1 = 678
    s1 = list(range(start1, end1))
    s1.append(duplicate1)
    assert findDuplicateNumber(s1, start1, end1) == duplicate1

    start2 = -123341
    end2 = 1123190
    duplicate2 = -2322
    s2 = list(range(start2, end2))
    s2.insert(len(s2) // 2, duplicate2)
    assert findDuplicateNumber(s2, start2, end2) == duplicate2
