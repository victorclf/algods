class Element:
    def __init__(self, key, originalIndex):
        self.key = key
        self.originalIndex = originalIndex
        self.inversions = 0

    def __gt__(self, other):
        return self.key > other.key


def _mergeWithInversionCounting(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    rightIndex = 0
    leftIndex = 0
    resultIndex = start

    inversions = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] > right[rightIndex]:
            arr[resultIndex] = right[rightIndex]
            inversions += 1
            rightIndex += 1
        else:
            arr[resultIndex] = left[leftIndex]
            arr[resultIndex].inversions += inversions
            leftIndex += 1
        resultIndex += 1

    while leftIndex < len(left):
        arr[resultIndex] = left[leftIndex]
        arr[resultIndex].inversions += inversions
        leftIndex += 1
        resultIndex += 1

    while rightIndex < len(right):
        arr[resultIndex] = right[rightIndex]
        rightIndex += 1
        resultIndex += 1


def _mergeSortWithInversionCounting(arr, start, end):
    if not (start + 1) < end:
        return

    mid = (start + end) // 2
    _mergeSortWithInversionCounting(arr, start, mid)
    _mergeSortWithInversionCounting(arr, mid, end)
    _mergeWithInversionCounting(arr, start, mid, end)


def countInversionsMergeSort(arr):
    """ For each element in arr, count how many inversions there are with objects to the right of it.
    Uses merge sort internally to achieve O(n logn) worst case complexity.

    >>> countInversionsMergeSort([5, 2, 6, 1])
    [2, 1, 1, 0]
    """
    arrObj = [Element(x, i) for i, x in enumerate(arr)]
    _mergeSortWithInversionCounting(arrObj, 0, len(arrObj))
    counts = [0] * len(arrObj)
    for x in arrObj:
        counts[x.originalIndex] = x.inversions
    return counts


# def countInversionsBisect(arr):
#     """ For each element in arr, count how many inversions there are with objects to the right of it.
#     Uses bisection algorithms internally but only achieves O(n^2) because of O(n) insertion on Python's dynamic array.
#
#     >>> countInversionsToTheRightMergeSort([5, 2, 6, 1])
#     [2, 1, 1, 0]
#     """
#
#     s = []
#     inversionsMap = []
#     for x in reversed(arr):
#         inversions = bisect.bisect_left(s, x)
#         bisect.insort_left(s, x)
#         inversionsMap.insert(0, inversions)
#     return inversionsMap


def _mergeWithTotalInversionCounting(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    rightIndex = 0
    leftIndex = 0
    resultIndex = start

    inversions = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] > right[rightIndex]:
            arr[resultIndex] = right[rightIndex]
            inversions += (len(left) - leftIndex)  # 1 inversion for each element remaining in the left array
            rightIndex += 1
        else:
            arr[resultIndex] = left[leftIndex]
            leftIndex += 1
        resultIndex += 1

    while leftIndex < len(left):
        arr[resultIndex] = left[leftIndex]
        leftIndex += 1
        resultIndex += 1

    while rightIndex < len(right):
        arr[resultIndex] = right[rightIndex]
        rightIndex += 1
        resultIndex += 1

    return inversions


def _mergeSortWithTotalInversionCounting(arr, start, end):
    if not (start + 1) < end:
        return 0

    mid = (start + end) // 2
    inversions = 0
    inversions += _mergeSortWithTotalInversionCounting(arr, start, mid)
    inversions += _mergeSortWithTotalInversionCounting(arr, mid, end)
    inversions += _mergeWithTotalInversionCounting(arr, start, mid, end)
    return inversions


def countInversions(arr):
    return _mergeSortWithTotalInversionCounting(arr, 0, len(arr))


if __name__ == '__main__':
    arr1 = [-76, -21, -99, -82, -29, -71, -11, -33, 3, -21, -45, -88, 96, -34, -88, 99, 62, -97, -4, -4, 67, -5, -6, -48, 92, -59, 56, 98, 34, 94, -27, 7, -21, 36, 50, -22, -10, -5, 58, 28, -60, 99, 0, -93, -79, -61, 82, -95, -5, 89, 91, 28, -20, 10, 40, -87, -27, -33, -30, -65, 70, -1, 90, 75, 30, -87, 72, 63, -17, -27, 13, -93, 88, 75, 75, 13, 60, -43, -1, -14, 43, 31, 32, 17, 62, 47, 78, -93, -9, 35, 89, -2, -38, -16, -66, -99, -25, -36, 71, -16, -95, 13, 10, -40, -52, 76, 65, -21, -12, -47, 70, -27, 27, 50, -91, -85, 34, -31, 76, 53, -57, -61, -20, 65, -18, -10, -80, -29, 92, -38, -100, -18, 10, -3, 83, 48, -8, -100, -65, -8, 36, 72, -47, 7, -77, 29, -52, 45, 7, -69, -15, -85, 65, -48, -62, -36, 29, 6, -92, -7, -63, -86, -58, -92, 24, -27, 33, -92, -24, 27, 10, -100, -78, 82, -42, -16, -46, 62, -30, -12, 74, -32, 4, 25, -67, -46, 41, 20, -24, 73, 42, 90, 90, 78, 75, 76, 81, 36, 85, -76, 43, -63, -72, -94, -96, 53, -37, 1, -56, -45, -4, 69, 52, -71, 62, 77, 75, -99, 85, 7, 78, -52, -6, -83, 85, -24, 6, 83, -7, 24, -42, 83, -30, -24, -20, 67, 32, 92, 55, 91, 17, 4, -32, 78, -93, -19, -20, -45, 48, -10, -84, -69, 70, -73, -5, 8, 36, -97, 93, -96, -60, -91, 99, 58, -8, 40, -76, -76, 0, -35, 12, -10, 26, 48, -52, -34, -89, 47, -32, -51, 42, -8, 23, 9, -65, 18, 30, 3, -99, -46, 35, -9, -11, -84, 60, 59, -4, -11, -23, 30, 51, -28, 36, -89, 54, -88, 64, -30, -9, 75, 68, -29, -24, 65, 37, -50, -56, 29, 17, -94, 90, -13, -28, -74, 28, 89, 85, 24, 42, -67, -33, -70, 78, -81, -67, -99, -1, -24, -44, 36, -83, -73, 87, -39, 13, -86, -64, 27, 66, -62, 36, 31, -63, 97, 0, -5, -27, -59, -42, -46, 26, 56, 57, 51, -51, 69, 62, -11, -3, 16, 47, -8, 57, -40, -55, 78, 59, -61, 0, -3, 24, 23, -39, 55, 96, 0, -84, -51, -18, -32, 6, -70, -43, -46, 38, 28, -5, -2, -57, -93, -66, -43, 58, 83, 14, 1, 32, 13, 54, 68, 12, -66, 97, -75, 67, 60, -6, 3, -51, 81, -82, -61, -18, 48, -7, -83, -58, 14, -82, 86, -8, -18, 84, 68, 52, 6, 93, 98, -90, 80, -29, -67, 31, 37, 24, -3, 26, 79, -22, -22, 16, 51, 1, -62, -22, 73, 73, 88, 65, 85, 0, -16, 84, 95, -99, -11, 96, 5, -13, 31, -37, 24, 45, 53, -84, 29, 19, 45, -82, -41, -51, 71, 87, 79, -81, -80, -12, -38, -42, 95, -17, 57, -87, -38, -13, 56, -57, -47, 66, 48, 22, -74, 72, 67, 81, 59, -59, 71, 11, -57, 67, -16, 24, 6, -50, -13, 21, -96, -33, -81, -11, -48, 94, 15, 18, 29, 39, 5, 30, -45, 49, -15, 22, 77, -17, -81, 20, -99, -99, -60, -51, 73, -62, 25, -25, 33, -86, -36, -25, 36, 28, 76, 23, 33, -98, -83, -7, -11, -32, 87, -10, 58, 53, 13, -41, -58, 31, -76, 5, -24, -76, -85, -58, 89, -18, 13, 96, -12, -10, 83, 97, -44, -92, -76, -66, 99, 37, 21, -94, 85, 26, 77, 83, -92, 95, 30, 72, -88, 97, -38, -71, -14, -81, -72, -12, 11, 92, 65, 41, -40, 34, -87, 43, 80, -23, -20, -19, 90, 94, -12, -89, 58, 27, -49, 4, 46, -37, -24, -41, 32, 4, -3, 55, -33, 37, 48, -14, 49, -21, 77, 88, 38, -48, -18, -69, -46, -69, -86, -16, 39, -20, 89, 50, 59, -52, -74, -50, 69, 95, -69, -77, 53, -71, 67, 41, 40, 54, -27, 5, 74, -76, -72, -79, 78, 28, 65, -64, 79, -95, -40, 82, -33, 23, 8, 69, 16, 70, 83, -65, 13, -53, -26, -95, 52, 0, 33, 56, 51, 26, 46, 22, -1, -97, -55, -82, 28, -66, -31, -96, 79, 63, 38, -40, -30, 54, 32, 19, -63, -88, -93, -37, 26, -46, -54, 76, -27, -81, 47, -17, 43, -2, 48, 30, -32, 63, -13, -82, -29, 9, -55, -28, -100, -18, -34, -22, -17, -97, -41, 10, -41, -60, 73, 8, 96, -41, 15, 31, -73, 80, 79, -61, -97, 64, 30, -94, 33, 73, 77, -22, 7, 58, 10, 64, 65, -51, 66, 57, -39, -13, -16, 89, 2, -94, -31, -45, 4, 99, -90, 63, 32, -87, -33, 19, 33, 35, -60, 82, 54, -48, 8, -62, 15, -34, 64, 93, 74, 15, -42, 88, -73, -36, 97, 6, 87, -31, 8, -83, -60, 1, -11, 47, 59, 26, 12, -95, 75, -43, 79, -98, -12, 37, -98, -24, -51, -66, -9, 14, 22, -66, 89, -36, 16, -82, -67, 5, -86, -34, -97, -47, -32, 13, 14, -88, 18, 40, 90, 63, -45, -69, -24, 68, -34, 54, 28, 83, -70, -23, -1, 80, 77, 54, -51, 98, 17, -31, 37, 41, 74, -22, 72, -8, -97, -68, -83, -10, 92, 82, 85, 5, -35, 75, 59, 60, -31, -15, 57, 18, 40, -97, -99, -35, -15, -59, -74, 95, -57, -42, -55, 83, -45, 40, 41, 36, 52, 96, -18, 1, -67, 43, 66, -4, 67, -65, -3, -95, 29, -33, 85, -72, 91, -2, 39, 16, -11, -82, 38, 55, 67, -22, -10, 78, -39, 24, -6, -54, 27, -59, -16, -27, 87, 5, 11, -7, 92, 30, -19, -41, 21, -45, -45, 80, 35, -83, 65, 79, 30, -75, 34, 68, -37, 64, -62, 47, -6, 54, -80, 92, -54, 77, -90, -69, 11, 15, 94, 64, 66, 27, 13, 13, 34, 3, -40, 90, 41, 89, 2, 10, 87, -21, 91]
    arr1 = arr1 * 100
    # print(countInversionsMergeSort(arr1))
    print(sum(countInversionsMergeSort(arr1)))
    print(countInversions(arr1))
    # a = countInversionsToTheRightMergeSort(arr1)
    # b = countInversionsBisect(arr1)