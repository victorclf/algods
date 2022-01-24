import enum

# TODO Reuse code from binary_search_tree


class Color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()


class Node:
    def __init__(self, key=None, value=None, parent=None, left=None, right=None, color=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return f'Node({str(self.key)})'

    def isChildOf(self, node):
        return self.parent is node

    def isParentOf(self, node):
        return self.left is node or self.right is node

    def isLeftChild(self):
        return self.parent.left is self

    def isRightChild(self):
        return self.parent.right is self

    def linkLeftChild(self, child):
        self.left = child
        child.parent = self

    def linkRightChild(self, child):
        self.right = child
        child.parent = self

    def isRed(self):
        return self.color == Color.RED

    def isBlack(self):
        return self.color == Color.BLACK


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, None, None, None, None, Color.BLACK)
        self.root = self.nil

    def __iter__(self):
        for node in self._nodes():
            yield node.key

    def _nodes(self):
        stack = []
        node = self.root
        while node is not self.nil or stack:
            if node is not self.nil:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right

    def items(self):
        for node in self._nodes():
            yield node.key, node.value

    def values(self):
        for node in self._nodes():
            yield node.value

    def _getNode(self, key):
        node = self.root
        while node is not self.nil:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError

    def get(self, key):
        return self._getNode(key).value

    def isRoot(self, node):
        return self.root is node

    def _minNode(self, node):
        if not node:
            raise KeyError
        while node.left is not self.nil:
            node = node.left
        return node

    def min(self):
        minNode = self._minNode(self.root)
        return minNode.key, minNode.value

    def _maxNode(self, node):
        if not node:
            raise KeyError
        while node.right is not self.nil:
            node = node.right
        return node

    def max(self):
        maxNode = self._maxNode(self.root)
        return maxNode.key, maxNode.value

    def _successorNode(self, node):
        if node.right is not self.nil:
            return self._minNode(node.right)
        x = node.parent
        while x is not self.nil and x.left != node:
            node = x
            x = x.parent
        return x

    def _predecessorNode(self, node):
        if node.left is not self.nil:
            return self._maxNode(node.left)
        x = node.parent
        while x is not self.nil and x.right != node:
            node = x
            x = x.parent
        return x

    def _createNode(self, key, value):
        return Node(key, value, self.nil, self.nil, self.nil, Color.RED)

    def _leftRotate(self, node):
        """ Changes node to be the left child of its current right child. """
        y = node.right
        node.linkRightChild(y.left)
        if self.isRoot(node):
            self.root = y
            y.parent = self.nil
        else:
            if node.isLeftChild():
                node.parent.linkLeftChild(y)
            else:
                node.parent.linkRightChild(y)
        y.linkLeftChild(node)

    def _rightRotate(self, node):
        """ Changes node to be the right child of its current left child. """
        y = node.left
        node.linkLeftChild(y.right)
        if self.isRoot(node):
            self.root = y
            y.parent = self.nil
        else:
            if node.isLeftChild():
                node.parent.linkLeftChild(y)
            else:
                node.parent.linkRightChild(y)
        y.linkRightChild(node)

    def _findPlaceToInsert(self, key):
        previousNode = self.nil
        currNode = self.root
        while currNode is not self.nil:
            previousNode = currNode
            currNode = currNode.left if key < currNode.key else currNode.right
        return previousNode

    def _insertFixup(self, node):
        while node.parent.isRed():
            if node.parent.isLeftChild():
                uncle = node.parent.parent.right
                if uncle.isRed():
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node.isRightChild():
                        node = node.parent
                        self._leftRotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rightRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.isRed():
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node.isLeftChild():
                        node = node.parent
                        self._rightRotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._leftRotate(node.parent.parent)
        self.root.color = Color.BLACK

    def put(self, key, value):
        newNode = self._createNode(key, value)
        parentNode = self._findPlaceToInsert(key)
        if parentNode is self.nil:
            self.root = newNode
        elif key < parentNode.key:
            parentNode.linkLeftChild(newNode)
        else:
            parentNode.linkRightChild(newNode)
        self._insertFixup(newNode)

    def _transplant(self, dstNode, srcNode):
        if dstNode.parent is self.nil:
            self.root = srcNode
            srcNode.parent = self.nil
        elif dstNode.isLeftChild():
            dstNode.parent.linkLeftChild(srcNode)
        else:
            dstNode.parent.linkRightChild(srcNode)

    def _deleteFixup(self, x):
        while x is not self.root and x.isBlack():
            if x.isLeftChild():
                w = x.parent.right
                if w.isRed():
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._leftRotate(x.parent)
                    w = x.parent.right
                if w.left.isBlack() and w.right.isBlack():
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.isBlack():
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._rightRotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.isRed():
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._rightRotate(x.parent)
                    w = x.parent.left
                if w.right.isBlack() and w.left.isBlack():
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.isBlack():
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._leftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._rightRotate(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def _popNode(self, z):
        y = z
        yOriginalColor = y.color
        if z.left is self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minNode(z.right)
            yOriginalColor = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.linkRightChild(z.right)
            self._transplant(z, y)
            y.linkLeftChild(z.left)
            y.color = z.color
        if yOriginalColor == Color.BLACK:
            self._deleteFixup(x)

    def pop(self, key):
        node = self._getNode(key)
        return self._popNode(node)
