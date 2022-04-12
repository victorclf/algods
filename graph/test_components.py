import unittest

from graph.components import findStronglyConnectedComponents, findConnectedComponents


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dag1 = [[1],  # a 0
                [2,4,5],  # b 1
                [3,6],  # c 2
                [2,7],  # d 3
                [0,5],  # e 4
                [6],  # f 5
                [5,7],  # g 6
                [7]]  # h 7
        self.undirectedGraph = [[1, 4],  # r = 0
                           [0, 5],  # s = 1
                           [3, 5, 6],  # t = 2
                           [2, 6, 7],  # u = 3
                           [0],  # v = 4
                           [1, 2, 6],  # w = 5
                           [2, 3, 5, 7],  # x = 6
                           [3, 6]]  # y = 7
        self.threeComponentGraph = [[1],
                               [0],
                               [3],
                               [2],
                               [5],
                               [4, 6],
                               [5]]
        self.directedGraph1 = [[3],
                               [0],
                               [1],
                               [4],
                               [1]]

    def testStronglyConnectedComponents(self):
        self.assertEqual(findStronglyConnectedComponents(self.dag1), [[1, 4, 0], [3, 2], [5, 6], [7]])
        self.assertEqual(findStronglyConnectedComponents(self.directedGraph1), [[2], [3, 4, 1, 0]])

    def testConnectedComponents(self):
        self.assertEqual(len(findConnectedComponents(self.undirectedGraph, isDirectedGraph=False)), 1)
        self.assertEqual(len(findConnectedComponents(self.threeComponentGraph, isDirectedGraph=False)), 3)


if __name__ == '__main__':
    unittest.main()
