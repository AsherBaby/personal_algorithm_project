def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    if len(s) == 0:
        return []

    ans = []
    getWord(s, wordDict, [], ans, set())
    return ans


def getWord(s, wordDict, path, ans, theUnbreakable):
    """
    path: list, list of words
    ans: list, answer of word break
    theUnbreakable: set, set of unbreakable words
    """
    if len(s) == 0:
        ans.append(' '.join(path))
        return True

    breakable = False
    for i in range(1, len(s)+1):
        if s[:i] in wordDict:
            path.append(s[:i])
            if s[i:] not in theUnbreakable:  # memorization
                breakable = getWord(s[i:], wordDict, path, ans, theUnbreakable) or breakable  # be careful about short-circuit
            path.pop()

    if not breakable:
        theUnbreakable.add(s)
    return breakable

s = 'catsanddog'
wordDict = {'cat', 'cats', 'and', 'dog', 'sand'}
ans = wordBreak(s, wordDict)
print(ans)