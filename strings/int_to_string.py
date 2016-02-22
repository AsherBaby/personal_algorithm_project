def str(int):
    ans = []
    while int:
        int, r = divmod(int, 10)
        ans.append(chr(r+ord('0')))
    return ''.join(reversed(ans))
