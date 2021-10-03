from sys import stdin
from collections import defaultdict, Counter

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7


for _ in range(rn()):
    n, k = rns()
    a = rl()
    tree = defaultdict(list)
    for __ in range(n - 1):
        x, y = rns()
        tree[x - 1].append(y - 1)
        tree[y - 1].append(x - 1)


    def dfs(root, parent, tree, xors, vals):
        ans = vals[root]
        for child in tree[root]:
            if child != parent:
                ans ^= dfs(child, root, tree, xors, vals)
        xors[root] = ans
        return ans


    ans = False

    xors = {}
    dfs(0, 0, tree, xors, a)  # parent is 1
    # print(xors)
    rest=xors[0]
    if rest==0:
        ans=True
    else:
        group = [i for i in xors if i!=0 and xors[i]==rest]

