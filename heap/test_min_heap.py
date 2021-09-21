import unittest
from heap.min_heap import MinHeap


def satisfiesMinHeapProperty(heap, i):
    if heap.exists(heap.left(i)) and heap.get(heap.left(i)) < heap.get(i):
        return False
    elif heap.exists(heap.right(i)) and heap.get(heap.right(i)) < heap.get(i):
        return False
    return True


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.l1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        self.h1 = MinHeap(self.l1)
        self.l2 = [-7, -2, -3, 4, 7, 9, 10, 14, 8, 16]
        self.h2 = MinHeap(self.l2)
        self.h3 = MinHeap([0, 2, 1, 4, 6, 3, 10, 14, 8, 16, 7, 9, 5])

    def test_create_heap(self):
        for i in range(len(self.h1)):
            self.assertTrue(satisfiesMinHeapProperty(self.h1, i))
        self.assertEqual(len(self.h1), len(self.l1))
        self.assertEqual(self.h1.min(), 1)

    def test_add(self):
        self.h1.add(6)
        self.h1.add(5)
        self.h1.add(0)

        self.assertTrue(6 in self.h1._list)
        self.assertTrue(5 in self.h1._list)
        self.assertTrue(0 in self.h1._list)
        for i in range(len(self.h1)):
            self.assertTrue(satisfiesMinHeapProperty(self.h1, i))

    def test_decrease(self):
        self.h2.decreaseKey(3, -9)
        self.assertTrue(self.h2.min(), -9)

    def test_decrease_error_bigger_key(self):
        with self.assertRaises(Exception):
            self.h2.decreaseKey(1, 100)

    # When last key smaller than removed key (5 < 6)
    def test_remove_last_key_smaller(self):
        previousLen = len(self.h3)

        self.assertEqual(self.h3.remove(4), 6)

        self.assertNotEqual(self.h3.get(4), 6)
        self.assertTrue(6 not in self.h3._list)
        self.assertEqual(len(self.h3), previousLen - 1)
        for i in range(len(self.h3)):
            self.assertTrue(satisfiesMinHeapProperty(self.h3, i))

    # When last key not smaller than removed key (9 > 3)
    def test_remove_last_key_not_smaller(self):
        previousLen = len(self.h3)

        self.assertEqual(self.h3.remove(5), 3)

        self.assertNotEqual(self.h3.get(5), 3)
        self.assertTrue(3 not in self.h3._list)
        self.assertEqual(len(self.h3), previousLen - 1)
        for i in range(len(self.h3)):
            self.assertTrue(satisfiesMinHeapProperty(self.h3, i))

    def test_remove_error_empty(self):
        while len(self.h1) > 0:
            self.h1.remove(0)

        try:
            self.h1.remove(0)
            assert False
        except IndexError:
            pass

    def test_remove_from_unitary_heap(self):
        unitHeap = MinHeap([7])

        self.assertEqual(unitHeap.remove(0), 7)


if __name__ == '__main__':
    unittest.main()
