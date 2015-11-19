def partition(s):
    result = []
    dfs([], s, result)
    return result

def dfs(nodes, s, result):
    if not s:
        result.append(nodes[:])
        return

    for i in range(len(s)):
        if valid(s[:i+1]):
            nodes.append(s[:i+1])
            dfs(nodes, s[i+1:], result)
            nodes.pop()

def valid(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

print(partition('aabbaba'))
