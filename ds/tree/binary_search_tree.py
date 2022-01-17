"""
Implementation of an unbalanced binary search tree.

"binary-search-tree property:
Let x be a node in a binary search tree. If y is a node in the left subtree
of x, then y.key <= x.key. If y is a node in the right subtree of x, then
y.key >= x.key."
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return f'Node({str(self.key)})'

    def isChildOf(self, node):
        return self.parent == node

    def isParentOf(self, node):
        return self.left == node or self.right == node

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def linkLeftChild(self, child):
        self.left = child
        if child:
            child.parent = self

    def linkRightChild(self, child):
        self.right = child
        if child:
            child.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        for node in self._nodes():
            yield node.key

    def _nodes(self):
        stack = []
        node = self.root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right if node.right else None

    def items(self):
        for node in self._nodes():
            yield node.key, node.value

    def values(self):
        for node in self._nodes():
            yield node.value

    def put(self, key, value):
        newNode = Node(key, value)

        if not self.root:
            self.root = newNode
            return

        node = self.root
        while True:
            if key == node.key:
                node.value = newNode.value
                return
            elif key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.linkLeftChild(newNode)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.linkRightChild(newNode)
                    return

    def _getNode(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError

    def get(self, key):
        return self._getNode(key).value

    def _minNode(self, node):
        if not node:
            raise KeyError
        while node.left:
            node = node.left
        return node

    def min(self):
        minNode = self._minNode(self.root)
        return minNode.key, minNode.value

    def _maxNode(self, node):
        if not node:
            raise KeyError
        while node.right:
            node = node.right
        return node

    def max(self):
        maxNode = self._maxNode(self.root)
        return maxNode.key, maxNode.value

    def _successorNode(self, node):
        if node.right:
            return self._minNode(node.right)
        x = node.parent
        while x and x.left != node:
            node = x
            x = x.parent
        return x

    def _predecessorNode(self, node):
        if node.left:
            return self._maxNode(node.left)
        x = node.parent
        while x and x.right != node:
            node = x
            x = x.parent
        return x

    def _transplant(self, dstNode, srcNode):
        if not dstNode.parent:
            self.root = srcNode
        elif dstNode.isLeftChild():
            dstNode.parent.linkLeftChild(srcNode)
        else:
            dstNode.parent.linkRightChild(srcNode)

    def _popNode(self, node):
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            y = self._minNode(node.right)
            if not y.isChildOf(node):
                self._transplant(y, y.right)
                y.linkRightChild(node.right)
            self._transplant(node, y)
            y.linkLeftChild(node.left)
        return node.value

    def pop(self, key):
        node = self._getNode(key)
        return self._popNode(node)
