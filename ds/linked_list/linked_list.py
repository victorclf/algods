class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def __iter__(self):
        currentNode = self.head
        while currentNode is not self.nil:
            yield currentNode.key
            currentNode = currentNode.next

    @property
    def head(self):
        return self.nil.next

    @head.setter
    def head(self, newHead):
        self.nil.next = newHead

    @property
    def tail(self):
        return self.nil.prev

    @tail.setter
    def tail(self, newTail):
        self.nil.prev = newTail

    def insertHead(self, key):
        self.insertHeadNode(Node(key))

    def insertHeadNode(self, node):
        self.head.prev = node
        node.next = self.head
        node.prev = self.nil
        self.head = node

    def search(self, key):
        currentNode = self.head
        self.nil.key = key
        while currentNode.key != key:
            currentNode = currentNode.next
        return currentNode if currentNode is not self.nil else None

    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise KeyError()
        self.deleteNode(node)

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
