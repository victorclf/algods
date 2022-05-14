import unittest

from graph.dfs import DFS


class DFSTestCase(unittest.TestCase):
    def setUp(self):
        self.directedGraph = [[1, 3],  # u = 0
                              [4],  # v = 1
                              [4, 5],  # w = 2
                              [1],  # x = 3
                              [3],  # y = 4
                              [5]]  # z = 5
    def testDFS(self):
        dfsDg1 = DFS(self.directedGraph, isDirectedGraph=True)
        dfsDg1.searchAllVertices()
        self.assertEqual(dfsDg1.parent, [None, 0, None, 4, 1, 2])
        self.assertTrue(all(dfsDg1.discovered))
        self.assertTrue(all(dfsDg1.processed))
        self.assertEqual(dfsDg1.entryTime, [1, 2, 9, 4, 3, 10])
        self.assertEqual(dfsDg1.exitTime, [8, 7, 12, 5, 6, 11])


if __name__ == '__main__':
    unittest.main()
