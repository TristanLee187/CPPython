rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    ans = 0
    n, k = rns()
    s = rs()
    a = 0
    for i in range(len(s) // 2):
        if s[i] != s[n - i - 1]:
            a += 1
    ans = abs(a - k)
    print('Case #' + str(_ + 1) + ': ' + str(ans))