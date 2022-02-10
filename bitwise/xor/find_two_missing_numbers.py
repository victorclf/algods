from collections import Counter


def findLowestBitSet(num):
    lowestBitPos = 0
    while num & 0b1 == 0:
        num >>= 1
        lowestBitPos += 1
    return lowestBitPos


def testBit(num, bitPos):
    bitMask = 0b1 << bitPos
    return num & bitMask


def generateSequenceWithoutBitPosSet(start, end, bitPos):
    bitMask = 0b1 << bitPos
    for i in range(start, end):
        if not testBit(i, bitPos):
            yield i


def findTwoMissingNumbers(sequence, startNumber, endNumber):
    '''
    Given a sequence [startNumber, endNumber) which is missing two numbers, finds those two missing numbers in O(n)
     time using XOR.

    :param sequence:
    :param startNumber:
    :param endNumber:
    :return: the missing number
    '''
    assert len(sequence) == (endNumber - startNumber) - 2

    fullSequenceXor = 0
    for i in range(startNumber, endNumber):
        fullSequenceXor ^= i

    actualSequenceXor = 0
    for i in sequence:
        actualSequenceXor ^= i

    missingNumbersXor = fullSequenceXor ^ actualSequenceXor
    assert missingNumbersXor != 0  # the XOR of two distinct numbers must be nonzero

    lowestBitSet = findLowestBitSet(missingNumbersXor)  # numbers differ at this bit

    actualSequenceWithoutBitXor = 0
    for i in sequence:
        if not testBit(i, lowestBitSet):
            actualSequenceWithoutBitXor ^= i

    fullSequenceWithoutBitXor = 0
    for i in generateSequenceWithoutBitPosSet(startNumber, endNumber, lowestBitSet):
        fullSequenceWithoutBitXor ^= i

    missingNumber1 = actualSequenceWithoutBitXor ^ fullSequenceWithoutBitXor
    missingNumber2 = missingNumbersXor ^ missingNumber1

    return missingNumber1, missingNumber2


if __name__ == '__main__':
    start1 = 341
    end1 = 1000
    missing1 = (498, 755)
    sequence1 = [x for x in range(start1, end1) if x not in missing1]
    assert Counter(findTwoMissingNumbers(sequence1, start1, end1)) == Counter(missing1)

    start2 = -123341
    end2 = 1123190
    missing2 = (-4980, 75501)
    sequence2 = [x for x in range(start2, end2) if x not in missing2]
    assert Counter(findTwoMissingNumbers(sequence2, start2, end2)) == Counter(missing2)
