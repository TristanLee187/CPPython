from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(2*10**5)
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    tree=defaultdict(list)
    root=-1
    for i in range(n):
        if i+1==a[i]:
            root=i+1
        else:
            tree[i+1].append(a[i])
            tree[a[i]].append(i+1)
    rootedtree=defaultdict(list)
    def poptree(rroot, par):
        for child in tree[rroot]:
            if child != par:
                rootedtree[rroot].append(child)
                poptree(child, rroot)
    poptree(root, root)
    # print(rootedtree)
    ans=[]
    def dfs(rroot, path):
        if rroot not in rootedtree:
            ans.append(path+[rroot])
        for j in range(len(rootedtree[rroot])):
            if j==0:
                dfs(rootedtree[rroot][j], path+[rroot])
            else:
                dfs(rootedtree[rroot][j], [])
    dfs(root, [])
    print(len(ans))
    for path in ans:
        print(len(path))
        print(*path)