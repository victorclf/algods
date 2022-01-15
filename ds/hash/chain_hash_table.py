import math
from ds.linked_list.linked_list import LinkedList


class Entry:
    def __init__(self, hash, key, value):
        self.hash = hash
        self.key = key
        self.value = value


class ChainHashTable:
    """
    Chaining hash table.
    """
    GOLDEN_RATIO = (math.sqrt(5) - 1) / 2

    def __init__(self, initialSize=0x10, loadFactor=0.75):
        if initialSize <= 0 or loadFactor <= 0:
            raise Exception()

        self._loadFactor = loadFactor
        self._nEntries = 0
        pow2InitialSize = 2 ** int(math.log2(initialSize))
        self._table = [LinkedList() for _ in range(pow2InitialSize)]

    def _hash(self, key):
        ownHash = hash(key)
        # Knuth Multiplication Hash
        knuthHash = int(((ownHash * ChainHashTable.GOLDEN_RATIO) % 1) * len(self._table))
        return knuthHash

    def _tableOverflow(self):
        return (self._nEntries / len(self._table)) > self._loadFactor

    def _resize(self):
        newSize = len(self._table) * 2
        oldTable = self._table
        self._table = [LinkedList() for _ in range(newSize)]  # remember that _hash() uses the length of self._table
        for l in oldTable:
            for entry in l:
                h = self._hash(entry.key)
                self._table[h].insertHead(Entry(h, entry.key, entry.value))

    def _getListNode(self, key):
        h = self._hash(key)
        l = self._table[h]
        for node in l.nodes():
            entry = node.element
            if entry.key == key:
                return l, node
        raise KeyError

    def _getEntry(self, key):
        lst, node = self._getListNode(key)
        return node.element

    def get(self, key):
        return self._getEntry(key).value

    def put(self, key, value):
        if self._tableOverflow():
            self._resize()
        h = self._hash(key)
        self._table[h].insertHead(Entry(h, key, value))
        self._nEntries += 1

    def pop(self, key):
        lst, node = self._getListNode(key)
        entry = node.element
        lst.deleteNode(node)
        self._nEntries -= 1
        return entry.value


if __name__ == '__main__':
    pass
