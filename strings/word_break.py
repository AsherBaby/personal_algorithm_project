"""
input:
    s = 'iamhappy'
    dictionary = {'i', 'am', 'happy', 'afternoon', 'after', 'noon'}
output version 1:
    ['i', 'am', 'happy']
output version 2:
    True

"""

def word_break1(s, d):
    # type: (str, set) => list
    """
    >>> s = 'afternoon'
    >>> d = {'i', 'am', 'happy', 'afternoon', 'after', 'noon'}
    >>> word_break1(s, d)
    [['after', 'noon'], ['afternoon']]
    """
    ans = []
    get_word(s, d, ans, [])
    return ans

def get_word(s, d, ans, words):
    if not s:
        ans.append(words[:])
        return
    for i in range(len(s)):
        if s[:i+1] in d:
            words.append(s[:i+1])
            get_word(s[i+1:], d, ans, words)
            words.pop()

def word_break2(s, d):
    # type: (str, set) => bool
    """
    >>> s = 'afternoon'
    >>> d = {'i', 'am', 'happy', 'afternoon', 'after', 'noon'}
    >>> word_break2(s, d)
    True
    """
    n = len(s)
    dp = [False] * (n+1)
    # dp[i] -> string[:i] is breakable
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            dp[i] = dp[i] or (dp[j] and s[j:i] in d)
    return dp[n]
