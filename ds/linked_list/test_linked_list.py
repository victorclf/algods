import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.elems1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        self.l1 = LinkedList()
        for e in reversed(self.elems1):
            self.l1.insertHead(e)
        self.nonexistentElem = 12345678

    def test_insert(self):
        for i, e in enumerate(self.l1):
            self.assertEqual(e, self.elems1[i])

    def test_search(self):
        elem = self.elems1[3]
        self.assertEqual(self.l1.search(elem).element, elem)

        self.assertIsNone(self.l1.search(self.nonexistentElem))

    def test_delete(self):
        self.l1.delete(self.elems1[0])
        self.elems1.pop(0)
        self.l1.delete(self.elems1[2])
        self.elems1.pop(2)
        self.l1.delete(self.elems1[3])
        self.elems1.pop(3)
        for i, e in enumerate(self.l1):
            self.assertEqual(e, self.elems1[i])

        with self.assertRaises(KeyError):
            self.l1.delete(self.nonexistentElem)


if __name__ == '__main__':
    unittest.main()
