from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
from math import gcd
from collections import defaultdict

for _ in range(rn()):
    n,q=rns()
    paths=[]
    for i in range(n-1):
        path=rl()
        paths.append(sorted(path[:2]) + path[2:])

    paths.sort()
    d=defaultdict(dict)
    for path in paths:
        d[path[0]][path[1]]=path[2:]
        d[path[1]][path[0]] = path[2:]

    paths={}
    def dfs(root,path,prev):
        paths[root]=path
        for other in d[root]:
            if other!=prev:
                dfs(other,path+[other],root)
    dfs(1,[1],1)

    ans=[]

    for i in range(q):
        c,w=rns()
        path = paths[c]
        app=0
        for j in range(len(path)-1):
            if w >= d[path[j]][path[j + 1]][0]:
                if app==0:
                    app=d[path[j]][path[j+1]][1]
                else:
                    app=gcd(app,d[path[j]][path[j+1]][1])
        ans.append(app)
    ans=' '.join(list(map(str,ans)))
    print('Case #' + str(_+1)+': ' + str(ans))