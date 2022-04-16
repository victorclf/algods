def buildZArray(s):
    """ Applies the Z algorithm on the string s and returns a list with the size of 
        the longest prefix-substring at each index of s.

    :param s: a sequence of elements
    :return list[int]: _description_
    """
    z = [0 for i in range(len(s))]
    l = r = 0
    for i in range(1, len(s)):
        k = i - l
        if i <= r and z[k] < r - i + 1:
            z[i] = z[k]
        else:
            l = r = i
            while r < len(s) and s[r] == s[r - i]:
                r += 1
            z[i] = r - l
            r -= 1  # r - 1 is the last character that satisfies condition
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

