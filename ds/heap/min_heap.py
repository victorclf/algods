import math


class MinHeap:
    """ Builds a min-heap from an list-like object. """

    def __init__(self, list_):
        """
        :param list_: list-like object to transform into heap
        """
        self._list = list_
        self._buildMinHeap()

    def _minHeapify(self, i):
        while self.exists(i):
            smallest = i

            l = self.left(i)
            r = self.right(i)
            if self.exists(l) and self._list[l] < self._list[smallest]:
                smallest = l
            if self.exists(r) and self._list[r] < self._list[smallest]:
                smallest = r

            if smallest != i:
                self._list[smallest], self._list[i] = self._list[i], self._list[smallest]
                i = smallest
            else:
                break

    def _buildMinHeap(self):
        for i in range((len(self._list) // 2) - 1, -1, -1):
            self._minHeapify(i)

    def __len__(self):
        return len(self._list)

    def add(self, e):
        self._list.append(e)
        lastIndex = len(self._list) - 1
        self.decreaseKey(lastIndex, e)

    def exists(self, i):
        return 0 <= i < len(self._list)

    def get(self, i):
        return self._list[i]

    def min(self):
        return self._list[0] if self._list else None

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def decreaseKey(self, i, newKey):
        if not self.exists(i) or newKey > self._list[i]:
            raise Exception()

        while self.exists(self.parent(i)) and newKey < self._list[self.parent(i)]:
            self._list[i] = self._list[self.parent(i)]
            i = self.parent(i)
        self._list[i] = newKey

    def remove(self, i):
        if not self.exists(i) or len(self._list) == 0:
            raise IndexError()

        removedKey = self._list[i]
        lastIndex = len(self._list) - 1
        lastKey = self._list[lastIndex]
        if not lastKey < self._list[i]:
            # key at last index cant be smaller than parent(i) but might violate heap property at i so we use heapify
            self._list[i] = lastKey
            self._minHeapify(i)
        else:
            # key at last index preserves heap property at i but might be smaller than parent(i) so use decrease key
            self.decreaseKey(i, lastKey)
        self._list.pop()
        return removedKey

    def __str__(self):
        levels = int(math.log2(len(self._list))) + 1
        i = 0
        heapStr = ''
        for l in range(levels):
            s = '  ' * (levels - l)
            n = 2 ** l
            s += '  '.join([str(x) for x in self._list[i:i + n]])
            i += n
            heapStr += s + '\n'
        return heapStr


if __name__ == '__main__':
    pass
