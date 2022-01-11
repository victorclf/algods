
# Algorithms for walking through a binary tree. Assumes the nodes have no parent attribute and don't modify the tree.
# Time complexity: O(n)
# Space complexity: O(n)


def recursivePreorderWalk(root, visitFunc):
    node = root
    if node:
        visitFunc(node)
        recursivePreorderWalk(node.left, visitFunc)
        recursivePreorderWalk(node.right, visitFunc)


def recursiveInorderWalk(root, visitFunc):
    node = root
    if node:
        recursiveInorderWalk(node.left, visitFunc)
        visitFunc(node)
        recursiveInorderWalk(node.right, visitFunc)


def recursivePostorderWalk(root, visitFunc):
    node = root
    if node:
        recursivePostorderWalk(node.left, visitFunc)
        recursivePostorderWalk(node.right, visitFunc)
        visitFunc(node)


def iterativePreorderWalk(root, visitFunc):
    stack = []
    node = root
    while node:
        visitFunc(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            node = node.left
        elif stack:
            node = stack.pop()
        else:
            break


def iterativeInorderWalk(root, visitFunc):
    stack = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            visitFunc(node)
            node = node.right if node.right else None


def iterativePostorderWalk(root, visitFunc):
    rightWalkStack = []
    visitStack = []
    node = root
    while node or visitStack:
        if node:
            if node.right:
                rightWalkStack.append(node.right)
            visitStack.append(node)
            node = node.left
        else:
            if rightWalkStack and visitStack[-1].right == rightWalkStack[-1]:
                node = rightWalkStack.pop()
            else:
                visitFunc(visitStack.pop())


if __name__ == '__main__':


    seq1 = []
    seq2 = []
    seq1Append = lambda node: seq.append(str(node))
    seq2Append = lambda node: seq.append(str(node))
    assert recursivePreorderWalk(nodes, visitFunc=seq1Append)

