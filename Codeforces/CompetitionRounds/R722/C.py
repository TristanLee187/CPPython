from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
from collections import defaultdict


for _ in range(rn()):
    n=rn()
    ranges = []
    for i in range(n):
        ranges.append(rl())
    tree = defaultdict(list)
    for i in range(n-1):
        u,v=rns()
        tree[u].append(v)
        tree[v].append(u)

    def dfs(root,parent):
        if len(tree[root])==1 and tree[root][0]==parent:
            return 0, 0
        else:
            choose_min = 0
            choose_max = 0
            for child in tree[root]:
                if child != parent:
                    a,b = dfs(child, root)
                    add = abs(ranges[child-1][0] - ranges[root-1][0]) + a
                    add = max(add, abs(ranges[child-1][1] - ranges[root-1][0]) + b)
                    choose_min += add

                    add = abs(ranges[child - 1][0] - ranges[root - 1][1]) + a
                    add = max(add, abs(ranges[child - 1][1] - ranges[root - 1][1]) + b)
                    choose_max += add
            return choose_min, choose_max
    a,b = dfs(1, -1)
    print(max(a, b))
