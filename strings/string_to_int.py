def int(str):
    sign, start = (True, 1) if str[0]=='-' else (False, 0)
    ans = 0
    for i in range(start, len(str)):
        ans *= 10
        ans += ord(str[i])-ord('0')
    return ans if not sign else -ans
