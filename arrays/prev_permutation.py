def prev_premutation(p):
    n = len(p)
    found = False
    for i in range(n-2, -1, -1):
        if p[i] > p[i+1]:
            found = True
            break
    if not found:
        return reversed(p)
    for j in range(n-1, i, -1):
        if p[j] < p[i]:
            break
    p[i], p[j] = p[j], p[i]
    p[i+1:] = reversed(p[i+1:])
    return p

print(list(prev_premutation([1])))
