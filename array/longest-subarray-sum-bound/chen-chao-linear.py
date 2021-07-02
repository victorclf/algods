#!/usr/bin/env python3


"""
Chen and Chao's algorithm for finding the longest subarray satisfying a sum bound.

IN:
    An array of real numbers `arr` and an inclusive lower bound `sumBound`.
OUT:
    A pair with the start and end index of the longest subarray of A with sum at least `sumBound`
    or (0, 0) if no subarray with sum at least `sumBound` exists.

Complexity:
    Time: O(n)

References:
- Optimal algorithms for locating the longest and shortest segments satisfying a sum or an average constraint,
Kuan-Yu Chen and Kun-Mao Chao, 2005
"""


def findLongestSubarraySumBounded(arr, sumBound):
    if not arr:
        return 0, 0

    n = len(arr)
    start = -1
    end = 0

    m = [0] * n  # array of safest indices. m[-1] = -1 (mathematical position for -1, not python index notation)
    mget = lambda index: m[index] if index >= 0 else -1
    c = [0] * n  # array of prefix sum. c[-1] = 0 (mathematical position for -1)
    cget = lambda index: c[index] if index >= 0 else 0

    for i in range(n):
        # Incrementally builds c on-the-fly.
        c[i] = cget(i - 1) + arr[i]

        # Incrementally builds m on-the-fly.
        if cget(i - 1) < cget(mget(i - 1)):
            m[i] = i - 1
        else:
            m[i] = mget(i - 1)

        # Test safest indices for a possible better answer than the current [start, end) for array [0, i + 1).
        k = i - end + start + 1
        while k >= 0:
            if cget(i) - cget(mget(k)) >= sumBound:
                k = mget(k)
            else:
                break
            start = k + 1
            end = i + 1

        # print(f"({start}, {end})")  # print best solution for subarray [0, i + 1)
    return (start, end) if start >= 0 else (0, 0)


if __name__ == '__main__':
    assert (findLongestSubarraySumBounded([], 1) == (0, 0))
    assert (findLongestSubarraySumBounded([-1, -1], 1) == (0, 0))
    # print(findLongestSubarraySumBounded([-1, -1, 1], 1))
    assert (findLongestSubarraySumBounded([-1, -1, 1], 1) == (2, 3))
    assert (findLongestSubarraySumBounded([1, 1, -1, -1, -1, -1, 1], 1) == (0, 3))
    assert (findLongestSubarraySumBounded([-1, 1, 1, -1, -1, 1, -1], 1) == (1, 6))
