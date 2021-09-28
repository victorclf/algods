#!/usr/bin/env python3

import collections

'''
Shunting Yard Algorithm

IN: 
    Infix expression
OUT:
    Postfix expression
    
Complexity:
    Time: O(n)
'''

Operator = collections.namedtuple('Operator', 'precedence associative')

# OPERATORS = {'&': Operator(1, 'left'), '|': Operator(1, 'left')}
OPERATORS = {'^': Operator(4, 'right'),
             '*': Operator(3, 'left'),
             '/': Operator(3, 'left'),
             '+': Operator(2, 'left'),
             '-': Operator(2, 'left')}
OPERANDS = tuple([str(x) for x in range(0, 10)])


# Shunting-yard algorithm
def convertInfixToPostfix(expr):
    operatorStack = []
    resultString = ''

    for e in expr:
        if e == '(':
            operatorStack.append(e)
        elif e == ')':
            while 1:
                p = operatorStack.pop()
                if p == '(':
                    break
                resultString += p
        elif e in OPERANDS:
            resultString += e
        elif e in OPERATORS:
            while 1:
                if not operatorStack or operatorStack[-1] == '(':
                    operatorStack.append(e)
                    break
                elif ((OPERATORS[e].precedence > OPERATORS[operatorStack[-1]].precedence)
                      or (OPERATORS[e].precedence == OPERATORS[operatorStack[-1]].precedence and OPERATORS[e].associative == 'right')):
                    operatorStack.append(e)
                    break
                elif ((OPERATORS[e].precedence < OPERATORS[operatorStack[-1]].precedence)
                          or (OPERATORS[e].precedence == OPERATORS[operatorStack[-1]].precedence and OPERATORS[e].associative == 'left')):
                    resultString += operatorStack.pop()
        else:
            raise Exception('Unexpected symbol:' + e)
    while operatorStack:
        resultString += operatorStack.pop()
    return resultString


if __name__ == '__main__':
    assert (convertInfixToPostfix('') == '')
    assert (convertInfixToPostfix('3+4*2/(1-5)^(((2))^3)') == '342*15-23^^/+')
    # assert (convertInfixToPostfix('1&(0|1)') == '101|&')
    # assert (convertInfixToPostfix('(0&0)&(0&0&0)') == '00&00&0&&')
    # assert (convertInfixToPostfix('(0|(1|0&1))') == '010|1&|')
