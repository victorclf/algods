import unittest
from collections import deque

from graph.sort import topologicalSort


class SortTestCase(unittest.TestCase):
    def testTopologicalSort(self):
        dag1 = [[1, 2],  #A 0
                [2, 3],  #B 1
                [4, 5],  #C 2
                [],  #D 3
                [3],  #E 4
                [4],  #F 5
                [0, 5]]  #G 6
        self.assertEqual(topologicalSort(dag1), deque([6, 0, 1, 2, 5, 4, 3]))


if __name__ == '__main__':
    unittest.main()
