from collections import namedtuple


def solveBinaryKnapsack(items, maxWeight):
    """ Find a subset of items which provide maximum value given a maximum weight constraint. Each item has a 'value'
    and 'weight'. This dynamic programming algorithm achieves O(nW) running time for n items and W maximum weight.

    :param items: objects with value and weight properties
    :param maxWeight: maximum weight allowed
    :returns: tuple with maximum value and list with the subset of items with that value
    """
    valueTable = [[0 for _ in range(maxWeight + 1)] for _ in range(len(items) + 1)]
    choiceTable = [[None for _ in range(maxWeight + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        item = items[i - 1]
        for j in range(1, maxWeight + 1):
            valueWithoutThisItem = valueTable[i - 1][j]
            valueWithThisItem = item.value + valueTable[i - 1][j - item.weight] if j >= item.weight else 0
            if valueWithThisItem >= valueWithoutThisItem:
                valueTable[i][j] = valueWithThisItem
                choiceTable[i][j] = i
            else:
                valueTable[i][j] = valueWithoutThisItem
                choiceTable[i][j] = choiceTable[i - 1][j]

    chosenItems = []
    i = len(items)
    j = maxWeight
    while i:
        item = items[i - 1]
        if i == choiceTable[i][j]:
            chosenItems.insert(0, item)
            i -= 1
            j -= item.weight
        else:
            i = choiceTable[i][j]
    return valueTable[-1][-1], chosenItems


if __name__ == '__main__':
    maxWeight = 67
    weights = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
    values = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]
    Item = namedtuple('Item', 'weight value')
    items = [Item(weights[i], values[i]) for i in range(len(weights))]
    solutionValue, solutionItems = solveBinaryKnapsack(items, maxWeight)
    assert solutionValue == 1270
    assert sum([i.value for i in solutionItems]) == 1270
    assert sum([i.weight for i in solutionItems]) <= maxWeight

