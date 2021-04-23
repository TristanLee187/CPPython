from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m=rns()
    grid=[]
    for i in range(n):
        grid.append(sorted(rl()))
    ans=[[] for i in range(n)]
    for i in range(m):
        k=0
        mins=float('inf')
        for j in range(n):
            if grid[j][0]<mins:
                mins=grid[j][0]
                k=j
        for j in range(n):
            if j==k:
                ans[j].append(grid[j].pop(0))
            else:
                ans[j].append(grid[j].pop())
    for i in ans:
        print(*i)