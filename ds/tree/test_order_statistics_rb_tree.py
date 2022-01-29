import unittest
from order_statistic_rb_tree import OrderStatisticRBTree, Node, Color


class TestOrderStatisticRBTree(unittest.TestCase):
    def setUp(self):
        self.keys1 = [4, 7, -1, 17, 13, 5, 6]
        self.values1 = ['zoltan', 'rockmen', 'engi', 'mantis', 'slug', 'human', 'crystal']
        self.sortedKeys1 = list(sorted(self.keys1))
        self.rb1 = OrderStatisticRBTree()
        for k, v in zip(self.keys1, self.values1):
            self.rb1.put(k, v)
        self.nonexistentKey = 1234

    def test_rank(self):
        for i, k in enumerate(self.sortedKeys1):
            self.assertEqual(self.rb1.rank(k), i)

    def test_rank_multiple_keys(self):
        keys = [1, 2, 2, 2, 3, 3, 4]
        values = list(range(len(keys)))
        rb = OrderStatisticRBTree()
        for k, v in zip(keys, values):
            rb.put(k, v)

        self.assertEqual(rb.rank(1), 0)
        self.assertEqual(rb.rank(2), 1)
        self.assertEqual(rb.rank(3), 4)
        self.assertEqual(rb.rank(4), 6)
        self.assertEqual(rb.rankRange(1), (0, 0))
        self.assertEqual(rb.rankRange(2), (1, 3))
        self.assertEqual(rb.rankRange(3), (4, 5))
        self.assertEqual(rb.rankRange(4), (6, 6))
        minRank2, maxRank2 = rb.rankRange(2)
        self.assertEqual(rb.getAll(2), values[minRank2:maxRank2 + 1])

    def test_select(self):
        for i, k in enumerate(self.sortedKeys1):
            self.assertEqual(self.rb1.select(i), k)

    def _validateSubtreeSize(self, node):
        self.assertEqual(node.subtreeSize, node.left.subtreeSize + node.right.subtreeSize + len(node.values))

    def _validateSubtreeSizes(self, tree):
        for node in tree._nodes():
            self._validateSubtreeSize(node)
        self.assertEqual(tree.root.subtreeSize, len(list(tree.values())))

    def test_put(self):
        rb = OrderStatisticRBTree()
        self.assertEqual(rb.root, rb.nil)
        value = "something"

        # Insert 41, 38, 31, 12, 19, 8 into empty tree. Covers all insert fixup cases.
        rb.put(41, value)
        self.assertEqual(rb.root.key, 41)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self._validateSubtreeSizes(rb)

        rb.put(38, value)
        self.assertEqual(rb.root.key, 41)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 38)
        self.assertTrue(rb.root.left.isRed())
        self._validateSubtreeSizes(rb)

        rb.put(31, value)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 31)
        self.assertTrue(rb.root.left.isRed())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isRed())
        self._validateSubtreeSizes(rb)

        rb.put(12, value)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 31)
        self.assertTrue(rb.root.left.isBlack())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self.assertEqual(rb.root.left.left.key, 12)
        self.assertTrue(rb.root.left.left.isRed())
        self._validateSubtreeSizes(rb)

        rb.put(19, value)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 19)
        self.assertTrue(rb.root.left.isBlack())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self.assertEqual(rb.root.left.left.key, 12)
        self.assertTrue(rb.root.left.left.isRed())
        self.assertEqual(rb.root.left.right.key, 31)
        self.assertTrue(rb.root.left.right.isRed())
        self._validateSubtreeSizes(rb)

        rb.put(8, value)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)

        self.assertEqual(rb.root.left.key, 19)
        self.assertTrue(rb.root.left.isRed())
        self.assertEqual(rb.root.left.parent, rb.root)

        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self.assertEqual(rb.root.right.parent, rb.root)

        self.assertEqual(rb.root.left.left.key, 12)
        self.assertTrue(rb.root.left.left.isBlack())
        self.assertEqual(rb.root.left.left.parent, rb.root.left)

        self.assertEqual(rb.root.left.right.key, 31)
        self.assertTrue(rb.root.left.right.isBlack())
        self.assertEqual(rb.root.left.right.parent, rb.root.left)

        self.assertEqual(rb.root.left.left.left.key, 8)
        self.assertTrue(rb.root.left.left.left.isRed())
        self.assertEqual(rb.root.left.left.left.parent, rb.root.left.left)

        self._validateSubtreeSizes(rb)

    def test_put2(self):
        keys = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
        v = None
        tree = OrderStatisticRBTree()
        for k in reversed(keys):
            tree.put(k, v)
            self._validateSubtreeSizes(tree)

    def test_put_none(self):
        tree = OrderStatisticRBTree()
        tree.put(None, None)
        tree.put(None, 5)
        self.assertEqual(tree.getAll(None), [None, 5])

    def test_put_get(self):
        for k, v in zip(self.keys1, self.values1):
            self.assertEqual(self.rb1.get(k), v)

    def test_iter(self):
        self.assertEqual(list(self.rb1), list(sorted(self.keys1)))

    def test_get_nonexistent(self):
        with self.assertRaises(KeyError):
            self.rb1.get(self.nonexistentKey)
    
    def test_pop(self):
        rb = OrderStatisticRBTree()
        value = "something"
        rb.put(41, value)
        rb.put(38, value)
        rb.put(31, value)
        rb.put(12, value)
        rb.put(19, value)
        rb.put(8, value)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 19)
        self.assertTrue(rb.root.left.isRed())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self.assertEqual(rb.root.left.left.key, 12)
        self.assertTrue(rb.root.left.left.isBlack())
        self.assertEqual(rb.root.left.right.key, 31)
        self.assertTrue(rb.root.left.right.isBlack())
        self.assertEqual(rb.root.left.left.left.key, 8)
        self.assertTrue(rb.root.left.left.left.isRed())
        self._validateSubtreeSizes(rb)

        # Remove 8, 12, 19, 31, 38, 41 from the tree.
        rb.pop(8)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 19)
        self.assertTrue(rb.root.left.isRed())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self.assertEqual(rb.root.left.left.key, 12)
        self.assertTrue(rb.root.left.left.isBlack())
        self.assertEqual(rb.root.left.right.key, 31)
        self.assertTrue(rb.root.left.right.isBlack())
        self._validateSubtreeSizes(rb)

        rb.pop(12)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 19)
        self.assertTrue(rb.root.left.isBlack())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self.assertEqual(rb.root.left.right.key, 31)
        self.assertTrue(rb.root.left.right.isRed())
        self._validateSubtreeSizes(rb)

        rb.pop(19)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 31)
        self.assertTrue(rb.root.left.isBlack())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())
        self._validateSubtreeSizes(rb)

        rb.pop(31)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isRed())
        self._validateSubtreeSizes(rb)

        rb.pop(38)
        self.assertEqual(rb.root.key, 41)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self._validateSubtreeSizes(rb)

        rb.pop(41)
        self.assertEqual(rb.root, rb.nil)
        self._validateSubtreeSizes(rb)

    def test_random(self):
        import random
        random.seed(42)
        keys = random.sample(range(-0xFF, 0xFF), 100)
        values = [random.randrange(-0xFF, 0xFF) for _ in range(len(keys))]
        bst = OrderStatisticRBTree()
        for k, v in zip(keys, values):
            bst.put(k, v)

        self.assertEqual(list(bst), list(sorted(keys)))
        self.assertEqual(bst.min()[0], min(keys))
        self.assertEqual(bst.max()[0], max(keys))
        self._validateSubtreeSizes(bst)


if __name__ == '__main__':
    unittest.main()
