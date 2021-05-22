from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))
from collections import defaultdict

n = rn()
p = rl()
a = []
for i in range(n - 1):
    a.append([p[i], i + 2])
a.sort()
del p
tree = defaultdict(list)
for pair in a:
    tree[pair[0]].append(pair[1])
del a


def dictadd(x, y):
    ans = defaultdict(int)
    for num in x:
        ans[num] += x[num]
    for num in y:
        ans[num] += y[num]
    return ans


def solve(root, counts, depth):
    ans = defaultdict(int)
    ans[depth]=1
    if root in tree:
        for num in tree[root]:
            ans = dictadd(ans, solve(num, counts, depth + 1))
    counts[root] = ans
    return ans


counts = [[] for i in range(n + 1)]
solve(1, counts, 1)
q = rn()
for i in range(q):
    u, d = rns()
    print(counts[u][d+1])
