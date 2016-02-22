ans = []
dict = {'i', 'am', 'happy', 'this', 'afternoon', 'after', 'noon'}

def word_break(s):
    get_word(s, [])

def get_word(s, seg):
    if not s:
        ans.append(seg[:])
        return
    for i in range(len(s)):
        if s[:i+1] in dict:
            seg.append(s[:i+1])
            get_word(s[i+1:], seg)
            seg.pop()

def word_break2(s):
    # O(n * w^2) algorithm
    # where w is the length of longest word in dict
    w = max([len(x) for x in dict]) if dict else 0
    n = len(s)
    can_break = [False] * (n+1)
    can_break[0] = True
    for i in range(1, n+1):
        for j in range(i-1, max(-1, i-1-w), -1):
            if s[j:i] in dict and can_break[j]:
                can_break[i] = True
                break
    return can_break[n]
