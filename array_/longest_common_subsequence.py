def _getLongestSubsequenceFromTable(x, y, c):
    i = len(x)
    j = len(y)
    seq = []
    while j > 0 and i > 0:
        if x[i - 1] == y[j - 1]:
            seq.append(x[i - 1])
            i -= 1
            j -= 1
        elif c[j][i - 1] >= c[j - 1][i]:
            i -= 1
        else:
            j -= 1
    return seq[::-1]


def _buildSubsequenceTable(x, y):
    c = [[0 for _ in range(len(x) + 1)] for _ in range(len(y) + 1)]
    for j in range(1, len(y) + 1):
        for i in range(1, len(x) + 1):
            if x[i - 1] == y[j - 1]:
                c[j][i] = c[j - 1][i - 1] + 1
            else:
                c[j][i] = max(c[j][i - 1], c[j - 1][i])
    return c


def findLongestCommonSubsequence(x, y):
    """ Finds a longest common subsequence of x and y. Subsequence differ from substring in that its
    elements do not need to be adjacent.

    Runtime complexity: O(m * n)
    Space complexity: O(m * n)

    :returns: a list with the longest common subsequence
    """
    table = _buildSubsequenceTable(x, y)
    return _getLongestSubsequenceFromTable(x, y, table)


def sizeOfLongestCommonSubsequence(x, y):
    """ Finds the size of the longest common subsequence of x and y. Subsequence differ from substring in that its
    elements do not need to be adjacent.

    Runtime complexity: O(m * n)
    Space complexity: O(min(m, n)) (can be reduced by using storing only one row during the loop below)
    """
    if len(y) < len(x):
        x, y = y, x

    prevRow = [0] * (len(x) + 1)
    row = [0]
    for j in range(1, len(y) + 1):
        for i in range(1, len(x) + 1):
            if x[i - 1] == y[j - 1]:
                row.append(prevRow[i - 1] + 1)
            else:
                row.append(max(row[i - 1], prevRow[i]))
        prevRow = row
        row = [0]
    return prevRow[-1]


if __name__ == '__main__':
    assert sizeOfLongestCommonSubsequence((), (0, 0, 0)) == 0
    assert sizeOfLongestCommonSubsequence([1], ()) == 0
    assert sizeOfLongestCommonSubsequence((1, 1, 1), (0, 0, 0)) == 0
    assert sizeOfLongestCommonSubsequence((1, 0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 1, 1, 0)) == 6
    assert sizeOfLongestCommonSubsequence('ABCDGH', 'AEDFHR') == 3 #adh
    assert sizeOfLongestCommonSubsequence('AGGTAB', 'GXTXAYB') == 4 #gtab

    assert findLongestCommonSubsequence((), (0, 0, 0)) == []
    assert findLongestCommonSubsequence([1], ()) == []
    assert findLongestCommonSubsequence((1, 1, 1), (0, 0, 0)) == []
    assert findLongestCommonSubsequence((1, 0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 1, 1, 0))
    assert findLongestCommonSubsequence('ABCDGH', 'AEDFHR') == ['A', 'D', 'H']
    assert findLongestCommonSubsequence('AGGTAB', 'GXTXAYB') == ['G', 'T', 'A', 'B']
