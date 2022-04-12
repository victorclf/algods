import unittest

from .bfs import BFS


def isUndirectedGraph(graph):
    edges = set()
    for u in range(len(graph)):
        for v in graph[u]:
            edges.add((u, v))

    for u, v in edges:
        if (v, u) not in edges:
            return False
    return True


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
        self.threeComponentGraph = [[1],
                               [0],
                               [3],
                               [2],
                               [5],
                               [4, 6],
                               [5]]
        self.twoColorableGraph = [[3, 4],
                             [4],
                             [4],
                             [0],
                             [0, 1, 2]]

    def testSearchVertex(self):
        self.assertTrue(isUndirectedGraph(self.undirectedGraph))
        self.assertTrue(isUndirectedGraph(self.threeComponentGraph))

        bfs = BFS(self.undirectedGraph, False).searchVertex(1)
        self.assertEqual(bfs.distance, [1, 0, 2, 3, 2, 1, 2, 3])
        self.assertEqual(bfs.parent, [1, None, 5, 2, 0, 1, 5, 6])
        self.assertTrue(all(bfs.discovered))


if __name__ == '__main__':
    unittest.main()
