from sys import stdin
from collections import defaultdict

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7

for _ in range(rn()):
    ans = 0
    n = rn()
    p = rs()
    d = defaultdict(list)
    colors = {
        'R': ['R'], 'B': ['B'], 'Y': ['Y'], 'O': ['R', 'Y'], 'P': ['R', 'B'], 'G': ['Y', 'B'],
        'A': ['R', 'Y', 'B'], 'U': ['U']
    }
    for i in range(n):
        for j in colors[p[i]]:
            d[j].append(i)
    # print(d)
    for color in d:
        if color == 'U':
            pass
        elif len(d[color]) == 1:
            ans += 1
        else:
            add = 1
            for i in range(1, len(d[color])):
                if d[color][i] - d[color][i - 1] > 1:
                    add += 1
            ans += add
    print('Case #' + str(_ + 1) + ': ' + str(ans))
