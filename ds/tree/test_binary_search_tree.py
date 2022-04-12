import unittest
from .binary_search_tree import BinarySearchTree, Node


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.keys1 = [4, 7, -1, 17, 13, 5, 6]
        self.values1 = ['zoltan', 'rockmen', 'engi', 'mantis', 'slug', 'human', 'crystal']
        self.sortedKeys1 = list(sorted(self.keys1))
        self.bst1 = BinarySearchTree()
        for k, v in zip(self.keys1, self.values1):
            self.bst1.put(k, v)
        self.nonexistentKey = 1234
        
    def test_put_get(self):
        for k, v in zip(self.keys1, self.values1):
            self.assertEqual(self.bst1.get(k), v)
        
    def test_iter(self):
        self.assertEqual(list(self.bst1), list(sorted(self.keys1)))

    def test_get_nonexistent(self):
        with self.assertRaises(KeyError):
            self.bst1.get(self.nonexistentKey)
    
    def test_pop(self):
        i = 1
        k = self.keys1.pop(i)
        v = self.values1.pop(i)
        self.assertEqual(self.bst1.pop(k), v)
        with self.assertRaises(KeyError):
            self.bst1.get(k)
        for k, v in zip(self.keys1, self.values1):
            self.assertEqual(self.bst1.get(k), v)

        k = self.keys1.pop(0)
        v = self.values1.pop(0)
        self.assertEqual(self.bst1.pop(k), v)

    def test_pop_root(self):
        self.bst1.pop(self.bst1.root.key)
        self.assertIsNone(self.bst1.root.parent)

    def test_random(self):
        import random
        random.seed(42)
        keys = random.sample(range(-0xFF, 0xFF), 100)
        values = [random.randrange(-0xFF, 0xFF) for _ in range(len(keys))]
        bst = BinarySearchTree()
        for k, v in zip(keys, values):
            bst.put(k, v)

        self.assertEqual(list(bst), list(sorted(keys)))
        self.assertEqual(bst.min()[0], min(keys))
        self.assertEqual(bst.max()[0], max(keys))


if __name__ == '__main__':
    unittest.main()
