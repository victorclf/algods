if __name__ == '__main__':
    '''
    Swap two variables without a third one using XOR.
    Works b/c not only is XOR associative and commutative but also (a ^ a == 0) and (a ^ 0 == a). 
    For reference purposes since integers are immutable in Python.
    '''
    a = -69105
    b = 40
    a ^= b
    b ^= a  # (a ^ b) ^ b == a ^ (b ^ b) == a
    a ^= b  # (a ^ b) ^ a == (a ^ a) ^ b == b
    assert a == 40
    assert b == -69105
