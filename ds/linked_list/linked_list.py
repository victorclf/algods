class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def __iter__(self):
        for x in self.nodes():
            yield x.element

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

    def nodes(self):
        currentNode = self.head
        while currentNode is not self.nil:
            yield currentNode
            currentNode = currentNode.next

    def insertHead(self, element):
        self.insertHeadNode(Node(element))

    def insertHeadNode(self, node):
        self.head.prev = node
        node.next = self.head
        node.prev = self.nil
        self.head = node

    def search(self, element):
        currentNode = self.head
        self.nil.element = element
        while currentNode.element != element:
            currentNode = currentNode.next
        return currentNode if currentNode is not self.nil else None

    def delete(self, element):
        node = self.search(element)
        if node is None:
            raise KeyError()
        self.deleteNode(node)

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
