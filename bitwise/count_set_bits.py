from multiprocessing.sharedctypes import Value
from typing import Type


def countSetBits(n):
    """Kernighan's algorithm to count set bits in a number. 
    
    WARN: algorithm does not support negative numbers because Python has arbitrary binary number precision and
    it uses sign-magnitude representation instead of two's complement. 

    :param int n: a number
    :raises ValueError: negative numbers not supported
    :return int: number of bits in n which are equal to 1
    """    
    if n < 0:
        raise ValueError("Negative numbers are not represented with two's complement in Python.")
    
    count = 0
    while n != 0:
        n &= n-1
        count += 1
    return count


if __name__ == '__main__':
    assert countSetBits(0b01010) == 2
    assert countSetBits(0b1111) == 4
    assert countSetBits(0b100001000111) == 5
    assert countSetBits(0b1000001) == 2
    assert countSetBits(0b00000) == 0
    try:
        countSetBits(-0b00001)
        assert False
    except ValueError:
        pass
    