t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = []
    for i in s:
        l.append(int(i))
    from math import ceil

    ans = sum(l[:ceil(n / 2)])
    curr = ans
    for i in range(ceil(n / 2), n):
        curr -= l[i - ceil(n / 2)]
        curr += l[i]
        ans = max(ans, curr)

    print('Case #' + str(_ + 1) + ': ' + str(ans))

