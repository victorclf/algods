import unittest

from graph.color import isTwoColorable


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.undirectedGraph = [[1, 4],  # r = 0
                           [0, 5],  # s = 1
                           [3, 5, 6],  # t = 2
                           [2, 6, 7],  # u = 3
                           [0],  # v = 4
                           [1, 2, 6],  # w = 5
                           [2, 3, 5, 7],  # x = 6
                           [3, 6]]  # y = 7
        self.twoColorableGraph = [[3, 4],
                             [4],
                             [4],
                             [0],
                             [0, 1, 2]]

    def testIsTwoColorable(self):
        self.assertFalse(isTwoColorable(self.undirectedGraph, isDirectedGraph=False))
        self.assertTrue(isTwoColorable(self.twoColorableGraph, isDirectedGraph=False))


if __name__ == '__main__':
    unittest.main()
