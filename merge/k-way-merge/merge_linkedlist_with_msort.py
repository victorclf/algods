import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # XXX
    # def __str__(self):
    #     s = ''
    #     node = self
    #     while node:
    #         s += f'{node.val} '
    #         node = node.next
    #     return s


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, a, b):
        cNodeBeforeHead = ListNode()
        cTail = cNodeBeforeHead

        while a and b:
            if a.val <= b.val:
                cTail.next = a
                cTail = a
                a = a.next
            else:
                cTail.next = b
                cTail = b
                b = b.next

        if a:
            cTail.next = a
        elif b:
            cTail.next = b

        return cNodeBeforeHead.next

    def mergeKLists(self, lists):
        while len(lists) > 1:
            newLists = []
            for i in range(len(lists) // 2):
                newLists.append(self.merge(lists[2*i], lists[2*i + 1]))
            if not len(lists) % 2 == 0:
                newLists.append(lists[-1])
            lists = newLists
        return lists[0] if lists else []


if __name__ == '__main__':
    lists = []
    for line in sys.stdin:
        elements = line.strip().split(' ')
        headNode = None
        previousNode = None
        for e in elements:
            node = ListNode(int(e))
            if headNode is None:
                headNode = node
            else:
                previousNode.next = node
            previousNode = node
        lists.append(headNode)

    result = Solution().mergeKLists(lists)
    # while result:
    #     print(result.val) #, end=' ')
    #     result = result.next
    # print()


