import unittest
from red_black_tree import RedBlackTree, Node, Color


class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.keys1 = [4, 7, -1, 17, 13, 5, 6]
        self.values1 = ['zoltan', 'rockmen', 'engi', 'mantis', 'slug', 'human', 'crystal']
        self.sortedKeys1 = list(sorted(self.keys1))
        self.rb1 = RedBlackTree()
        for k, v in zip(self.keys1, self.values1):
            self.rb1.put(k, v)
        self.nonexistentKey = 1234

    def test_put(self):
        rb = RedBlackTree()
        self.assertEqual(rb.root, rb.nil)
        value = "something"

        # Insert 41, 38, 31, 12, 19, 8 into empty tree. Covers all insert fixup cases.
        rb.put(41, value)
        self.assertEqual(rb.root.key, 41)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)

        rb.put(38, value)
        self.assertEqual(rb.root.key, 41)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 38)
        self.assertTrue(rb.root.left.isRed())

        rb.put(31, value)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 31)
        self.assertTrue(rb.root.left.isRed())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isRed())

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

    def test_put_get(self):
        for k, v in zip(self.keys1, self.values1):
            self.assertEqual(self.rb1.get(k), v)

    def test_iter(self):
        self.assertEqual(list(self.rb1), list(sorted(self.keys1)))

    def test_get_nonexistent(self):
        with self.assertRaises(KeyError):
            self.rb1.get(self.nonexistentKey)
    
    def test_pop(self):
        rb = RedBlackTree()
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

        rb.pop(19)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.left.key, 31)
        self.assertTrue(rb.root.left.isBlack())
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isBlack())

        rb.pop(31)
        self.assertEqual(rb.root.key, 38)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)
        self.assertEqual(rb.root.right.key, 41)
        self.assertTrue(rb.root.right.isRed())

        rb.pop(38)
        self.assertEqual(rb.root.key, 41)
        self.assertTrue(rb.root.isBlack())
        self.assertEqual(rb.root.parent, rb.nil)

        rb.pop(41)
        self.assertEqual(rb.root, rb.nil)

    def test_random(self):
        import random
        random.seed(42)
        keys = random.sample(range(-0xFF, 0xFF), 100)
        values = [random.randrange(-0xFF, 0xFF) for _ in range(len(keys))]
        bst = RedBlackTree()
        for k, v in zip(keys, values):
            bst.put(k, v)

        self.assertEqual(list(bst), list(sorted(keys)))
        self.assertEqual(bst.min()[0], min(keys))
        self.assertEqual(bst.max()[0], max(keys))


if __name__ == '__main__':
    unittest.main()
