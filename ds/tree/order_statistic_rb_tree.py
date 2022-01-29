import enum

class Color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()


class Node:
    def __init__(self, key=None, value=None, parent=None, left=None, right=None, color=None):
        self.key = key
        self.values = [value]
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color
        self.subtreeSize = 1

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

    def updateSubtreeSize(self):
        self.subtreeSize = len(self.values)
        self.subtreeSize += self.left.subtreeSize if self.left else 0
        self.subtreeSize += self.right.subtreeSize if self.right else 0

    def appendValue(self, v):
        self.values.append(v)
        self.updateSubtreeSize()


class NilNode(Node):
    def __init__(self):
        super().__init__(None, None, None, None, None, Color.BLACK)
        self.values = []
        self.subtreeSize = 0


class OrderStatisticRBTree:
    """Order statistic tree built on red-black tree. Supports multiple values for a key by storing them
    in the same node. """

    def __init__(self):
        self.nil = NilNode()
        self.root = self.nil

    def __iter__(self):
        for node in self._nodes():
            yield node.key

    def __len__(self):
        return self.root.subtreeSize

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
            for v in node.values:
                yield node.key, v

    def values(self):
        for node in self._nodes():
            for v in node.values:
                yield v

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
        return self._getNode(key).values[0]

    def getAll(self, key):
        return self._getNode(key).values

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
        return minNode.key, minNode.values[0]

    def _maxNode(self, node):
        if not node:
            raise KeyError
        while node.right is not self.nil:
            node = node.right
        return node

    def max(self):
        maxNode = self._maxNode(self.root)
        return maxNode.key, maxNode.values[0]

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
        node = Node(key, value, self.nil, self.nil, self.nil, Color.RED)
        return node

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
        node.updateSubtreeSize()
        y.updateSubtreeSize()

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
        node.updateSubtreeSize()
        y.updateSubtreeSize()

    def _findPlaceToInsert(self, key):
        """ Traverses the tree until it finds the appropriate parent node for the new node with the given key.
        Importantly, also increments the subtreeSize of each node on the path.
        """
        previousNode = self.nil
        currNode = self.root
        while currNode is not self.nil:
            currNode.subtreeSize += 1
            if currNode.key == key:
                return currNode
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
        parentNode = self._findPlaceToInsert(key)

        if parentNode is not self.nil and key == parentNode.key:  # node with key already exists. just add value to this node
            parentNode.appendValue(value)
            return

        newNode = self._createNode(key, value)
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

    def _decrementSubtreeSizesOfParents(self, node, sizeDecrement):
        node = node.parent  # doesnt include node itself in the update
        while node is not self.nil:
            node.subtreeSize -= sizeDecrement
            node = node.parent

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
        self._decrementSubtreeSizesOfParents(y, len(z.values))
        if yOriginalColor == Color.BLACK:
            self._deleteFixup(x)
        return z.values

    def pop(self, key):
        """ Removes all values matching the given key and return them as a list. """
        node = self._getNode(key)
        return self._popNode(node)

    def _rankNode(self, node):
        rank = node.left.subtreeSize
        while node.parent is not self.nil:
            if node.isRightChild():
                rank += node.parent.left.subtreeSize + len(node.parent.values)
            node = node.parent
        return rank

    def rank(self, key):
        """ Returns the 0-based rank of the key in the red-black tree. In case of multiple values, return the minimum
        rank for that key. """
        node = self._getNode(key)
        return self._rankNode(node)

    def rankRange(self, key):
        """ Returns the 0-based minimum and maximum ranks of the key in the red-black tree. A key has multiple ranks
        when it has multiple values. """
        node = self._getNode(key)
        minRank = self._rankNode(node)
        maxRank = minRank + len(node.values) - 1
        return minRank, maxRank

    def select(self, rank):
        """ Returns the key in the red-black tree matching the given the 0-based rank."""
        node = self.root
        while node is not self.nil:
            if rank == node.left.subtreeSize:
                return node.key
            elif rank < node.left.subtreeSize:
                node = node.left
            else:
                rank -= (node.left.subtreeSize + len(node.values))
                node = node.right
        raise ValueError
