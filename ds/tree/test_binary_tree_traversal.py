import unittest
from binary_tree_traversal import *


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return f'TreeNode({str(self.key)})'


class TestBinaryTreeTraversal(unittest.TestCase):
    def setUp(self):
        """
                                            0
                       /                                      \
                    1                                          2
              /         \                           /                     \
            3             4                       5                        6
          /                 \                       \                     /
        7                     8                      9                  10
                                                       \
                                                         11
        """
        nodes = [TreeNode(key) for key in range(12)]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]
        nodes[1].left = nodes[3]
        nodes[1].right = nodes[4]
        nodes[2].left = nodes[5]
        nodes[2].right = nodes[6]
        nodes[3].left = nodes[7]
        nodes[4].right = nodes[8]
        nodes[5].right = nodes[9]
        nodes[6].left = nodes[10]
        nodes[9].right = nodes[11]
        self.root = nodes[0]

        self.seq1 = []
        self.seq2 = []
        self.visitSeq1 = lambda node: self.seq1.append(str(node))
        self.visitSeq2 = lambda node: self.seq2.append(str(node))

    def testIterativePreorderWalk(self):
        recursivePreorderWalk(self.root, self.visitSeq1)
        iterativePreorderWalk(self.root, self.visitSeq2)
        self.assertEqual(self.seq1, self.seq2)
        self.assertEqual(self.seq1, ['0', '1', '3', '7', '4', '8', '2', '5', '9', '11', '6', '10'])

    def testIterativeInorderWalk(self):
        recursiveInorderWalk(self.root, self.visitSeq1)
        iterativeInorderWalk(self.root, self.visitSeq2)
        self.assertEqual(self.seq1, self.seq2)
        self.assertEqual(self.seq1, ['7', '3', '1', '4', '8', '0', '5', '9', '11', '2', '10', '6'])

    def testIterativePostorderWalk(self):
        recursivePostorderWalk(self.root, self.visitSeq1)
        iterativePostorderWalk(self.root, self.visitSeq2)
        self.assertEqual(self.seq1, self.seq2)
        self.assertEqual(self.seq1, ['7', '3', '8', '4', '1', '11', '9', '5', '10', '6', '2', '0'])


if __name__ == '__main__':
    unittest.main()
