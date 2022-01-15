import unittest
from chain_hash_table import ChainHashTable


class TestChainHashTable(unittest.TestCase):
    def setUp(self):
        self.keys1 = ['doom', 'doom2', 'duke3d', 'wolf3d', 'quake']
        self.values1 = [1993, 1994, 1996, 1992, 1996]
        self.ht1 = ChainHashTable()
        for i, k in enumerate(self.keys1):
            v = self.values1[i]
            self.ht1.put(k, v)
        self.nonexistentKey = 'bigrigs'

    def test_put_get(self):
        for i, k in enumerate(self.keys1):
            v = self.values1[i]
            self.assertEqual(self.ht1.get(k), v)

    def test_get_nonexistent(self):
        with self.assertRaises(KeyError):
            self.ht1.get(self.nonexistentKey)

    def test_pop(self):
        i = 1
        k = self.keys1.pop(i)
        v = self.values1.pop(i)
        self.assertEqual(self.ht1.pop(k), v)
        with self.assertRaises(KeyError):
            self.ht1.get(k)
        for i, k in enumerate(self.keys1):
            v = self.values1[i]
            self.assertEqual(self.ht1.get(k), v)

    def test_dynamic_resize(self):
        initialSize = 5
        ht = ChainHashTable(initialSize)
        keys = list(range(50))
        values = [k * 7 for k in keys]
        for i, k in enumerate(keys):
            v = values[i]
            ht.put(k, v)
        for i, k in enumerate(keys):
            v = values[i]
            self.assertEqual(ht.get(k), v)


if __name__ == '__main__':
    unittest.main()
