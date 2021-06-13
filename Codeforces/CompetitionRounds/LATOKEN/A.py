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
        grid.append(list(rs().strip()))
    ans=True
    r=-1
    w=-1
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='R':
                if (i+j)%2==w:
                    ans=False
                    break
                if r==-1:
                    r=(i+j)%2
                elif (i+j)%2!=r:
                    ans=False
                    break
            elif grid[i][j] == 'W':
                if (i+j)%2==r:
                    ans=False
                    break
                if w == -1:
                    w = (i + j) % 2
                elif (i + j) % 2 != w:
                    ans = False
                    break
    YN(ans)
    if ans:
        if r==-1==w:
            r=0
            w=1
        elif r==-1:
            r=int(not w)
        elif w==-1:
            w=int(not r)
        colors=['','']
        colors[r]='R'
        colors[w]='W'
        for i in range(n):
            for j in range(m):
                grid[i][j]=colors[(i+j)%2]
        for row in grid:
            print(''.join(row))

