t = int(input())
for i in range(t) :
    s= input()
    cur = 0
    res = 0
    for i in range(len(s)):
        if s[i] == '+':
            cur += 1
        else:
            cur -= 1
        if cur < 0:
            res += i + 1
            cur = 0
    print(res + len(s))
