import operator
from typing import Iterable, List


def _findElements(arr: Iterable, comparisonFn, previousElements=False):
    n = len(arr)
    result = [None] * n
    stack = []  # a monotonic stack
    gen = enumerate(arr) if not previousElements else reversed(
        list(enumerate(arr)))
    for i, e in gen:
        while stack and comparisonFn(e, arr[stack[-1]]):
            result[stack.pop()] = i
        stack.append(i)
    return result


def findPreviousGreaterElements(arr: Iterable):
    """ For each element in arr, finds the index of closest previous (to its left) greater element or None if no such element exists.

    Time: O(n)

    :param Iterable arr: an iterable with elements that can be compared with < (less than operator)
    :return list: a list prev where prev[i] is the index of the first element to the left of arr[i] which is greater than it or prev[i] is None if no such element exists.
    """
    return _findElements(arr, operator.gt, previousElements=True)


def findNextGreaterElements(arr: Iterable):
    """ For each element in arr, finds the index of closest next (to its right) greater element or None if no such element exists.

    Time: O(n)

    :param Iterable arr: an iterable with elements that can be compared with < (less than operator)
    :return list: a list next where next[i] is the index of the first element to the right of arr[i] which is greater than it or next[i] is None if no such element exists.
    """
    return _findElements(arr, operator.gt, previousElements=False)


def findPreviousSmallerElements(arr: Iterable):
    """ For each element in arr, finds the index of closest previous (to its left) smaller element or None if no such element exists.

    Time: O(n)

    :param Iterable arr: an iterable with elements that can be compared with < (less than operator)
    :return list: a list prev where prev[i] is the index of the first element to the left of arr[i] which is smaller than it or prev[i] is None if no such element exists.
    """
    return _findElements(arr, operator.lt, previousElements=True)


def findNextSmallerElements(arr: Iterable):
    """ For each element in arr, finds the index of closest next (to its right) smaller element or None if no such element exists.

    Time: O(n)

    :param Iterable arr: an iterable with elements that can be compared with < (less than operator)
    :return list: a list next where next[i] is the index of the first element to the right of arr[i] which is smaller than it or next[i] is None if no such element exists.
    """
    return _findElements(arr, operator.lt, previousElements=False)


###
# Easier to understand non-generic implementations
###
def _findPreviousSmallerElementsEasy(arr: Iterable):
    """ For each element in arr, finds the index of closest previous (to its left) smaller element or None if no such element exists.

    Time: O(n)

    :param Iterable arr: an iterable with elements that can be compared with < (less than operator)
    :return list: a list prev where prev[i] is the index of the first element to the left of arr[i] which is smaller than it or prev[i] is None if no such element exists.
    """
    n = len(arr)
    prev = [None] * n
    stack = []  # a monotonically nondecreasing stack
    
    for i, e in reversed(list(enumerate(arr))): # cant do reversed(enumerate()) without a list
        while stack and e < arr[stack[-1]]:
            prev[stack.pop()] = i
        stack.append(i)
        
    return prev


def _findNextSmallerElementsEasy(arr: Iterable):
    """ For each element in arr, finds the index of closest next (to its right) smaller element or None if no such element exists.

    Time: O(n)

    :param Iterable arr: an iterable with elements that can be compared with < (less than operator)
    :return list: a list next where next[i] is the index of the first element to the right of arr[i] which is smaller than it or next[i] is None if no such element exists.
    """
    n = len(arr)
    next = [None] * n
    stack = []  # a monotonically nondecreasing stack
    
    for i, e in enumerate(arr):
        while stack and e < arr[stack[-1]]:
            next[stack.pop()] = i
        stack.append(i)
        
    return next


if __name__ == '__main__':
    assert findPreviousSmallerElements([0, 1, 2, 3, 4]) == [None, 0, 1, 2, 3]
    assert findPreviousSmallerElements([2, 1, 4, 3, 4]) == [
        None, None, 1, 1, 3]

    assert findNextSmallerElements([0, 1, 2, 3, 4]) == [
        None, None, None, None, None]
    assert findNextSmallerElements([4, 3, 2, 1, 0]) == [1, 2, 3, 4, None]
    assert findNextSmallerElements([2, 1, 4, 3, 4]) == [1, None, 3, None, None]

    assert findPreviousGreaterElements([0, 1, 2, 3, 4]) == [
        None, None, None, None, None]

    assert findNextGreaterElements([2, 1, 4, 3, 4]) == [2, 2, None, 4, None]
