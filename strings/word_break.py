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

word_break('iamhappythisafternoon')
print(ans)
