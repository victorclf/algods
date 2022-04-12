import unittest

from graph.cycle import isCyclicGraph


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cyclicGraph = [[1],
                  [2],
                  [0]]
        self.acyclicGraph = [[1],
                  [2],
                  []]
        self.directedGraph = [[1, 3],  # u = 0
                              [4],  # v = 1
                              [4, 5],  # w = 2
                              [1],  # x = 3
                              [3],  # y = 4
                              [5]]

    def testIsCyclicGraph(self):
        self.assertFalse(isCyclicGraph(self.acyclicGraph, isDirectedGraph=False))
        self.assertTrue(isCyclicGraph(self.cyclicGraph, isDirectedGraph=False))
        self.assertTrue(isCyclicGraph(self.directedGraph, isDirectedGraph=True))


if __name__ == '__main__':
    unittest.main()
