def buildZArray(s):
    """ Applies the Z algorithm on the string s and returns a list with the size of 
        the longest prefix-substring at each index of s.

    :param s: a sequence of elements
    :return list[int]: Z array with longest prefix-substring at each index of s
    """
    n = len(s)
    z = [0 for i in range(n)]
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


def iterAllMatches(text, pattern, uniqueCharacter='^'):
    """ Iterates through all occurrences of pattern in text.

    :param str text: text
    :param str pattern: pattern
    :param str uniqueCharacter: a separator character that does not occur in either text or pattern, defaults to '^'
    :yield int: index of match
    """
    if not pattern:
        return
    
    z = buildZArray(f'{pattern}{uniqueCharacter}{text}')
    for i in range(0, len(text)):
        if z[i + len(pattern) + len(uniqueCharacter)] == len(pattern):  # adjust index b/c of prefix {pattern}{uniqueCharacter}
            yield i


def countMatches(text, pattern, uniqueCharacter='^'):
    """ Counts all occurrences of pattern in text (case sensitive).

    :param str text: text
    :param str pattern: pattern
    :param str uniqueCharacter: a separator character that does not occur in either text or pattern, defaults to '^'
    :return int: number of pattern matches in the text
    """
    if not pattern:
        return 0
    
    z = buildZArray(f'{pattern}{uniqueCharacter}{text}')
    return z.count(len(pattern))

