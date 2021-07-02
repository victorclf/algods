#!/usr/bin/env python3

"""
Parse a postfix expression with binary operators to an abstract syntax tree (AST).

IN:
	Postfix expression without spaces and elements represented by a single char.
    
OUT:
    Root of an AST representing the expression

Complexity:
    Time: O(n)
"""

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self._result = None

class AndNode(Node):
    @property
    def result(self):
        if self._result is None:
            self._result = self.left.result & self.right.result
        return self._result


class OrNode(Node):
    @property
    def result(self):
        if self._result is None:
            self._result = self.left.result | self.right.result
        return self._result


class ValueNode(Node):
    def __init__(self, value):
        self.value = int(value)

    @property
    def result(self):
        return self.value

OPERATORS = {'&': AndNode, '|': OrNode}

def parsePostfix(expr):
    s = []
    for e in expr:
        if e not in OPERATORS:
            s.append(ValueNode(e))
        else:
            right = s.pop()
            left = s.pop()
            opNode = OPERATORS[e](left, right)
            s.append(opNode)
    return s.pop()
