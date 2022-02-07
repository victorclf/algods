def _findLongestIncreasingSubsequenceQuadratic(arr):
    from longest_common_subsequence import findLongestCommonSubsequence
    return findLongestCommonSubsequence(arr, sorted(arr))


class Node:
    def __init__(self, element, prevNode):
        self.element = element
        self.prevNode = prevNode

    def __repr__(self):
        return f'{self.element}'


def findLongestIncreasingSubsequence(arr):
    """ Finds a longest monotonically increasing (never decreases) subsequence. """
    piles = []
    for e in arr:
        if not piles:
            piles.append([Node(e, None)])
            continue

        a = 0
        b = len(piles)
        bestPossiblePile = None
        while a < b:
            mid = (a + b) // 2
            if piles[mid][-1].element >= e:
                bestPossiblePile = mid
                b = mid
            else:
                a = mid + 1

        if bestPossiblePile is not None:
            # Found suitable pile for this element.
            prevNode = None
            if piles[bestPossiblePile][-1].element == e:
                prevNode = piles[bestPossiblePile][-1]
            elif bestPossiblePile > 0:
                prevNode = piles[bestPossiblePile - 1][-1]
            piles[bestPossiblePile].append(Node(e, prevNode))
        else:
            # No suitable pile for this element. Create new one.
            prevNode = piles[-1][-1]
            piles.append([Node(e, prevNode)])

    subsequence = []
    if piles:
        node = piles[-1][-1]
        while node:
            subsequence.insert(0, node.element)
            node = node.prevNode
    return subsequence


if __name__ == '__main__':
    def isIncreasingSubsequence(seq, subseq):
        i = 0
        lastElement = subseq[0] if subseq else None
        for e in subseq:
            if e < lastElement:
                return False
            lastElement = e

            try:
                i = seq.index(e, i) + 1
            except ValueError:
                return False

        return True


    seq = [2, 4, 3, 5, 1, 7, 6, 9, 8] * 3
    print(seq)

    print()
    print(_findLongestIncreasingSubsequenceQuadratic(seq))
    assert isIncreasingSubsequence(seq, _findLongestIncreasingSubsequenceQuadratic(seq))
    assert len(_findLongestIncreasingSubsequenceQuadratic(seq)) == 7

    print()
    print(findLongestIncreasingSubsequence(seq))
    assert isIncreasingSubsequence(seq, findLongestIncreasingSubsequence(seq))
    assert len(findLongestIncreasingSubsequence(seq)) == 7
