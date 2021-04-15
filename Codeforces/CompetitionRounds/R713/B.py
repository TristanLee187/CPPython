rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    grid=[]
    for i in range(n):
        grid.append(list(rs()))
    l=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='*':
                l.append([i,j])

    if l[0][0]==l[1][0]:
        l[0][0] = l[1][0] = 0 if l[0][0]!=0 else 1
    elif l[0][1]==l[1][1]:
        l[0][1] = l[1][1] = 0 if l[0][1]!=0 else 1
    grid[l[0][0]][l[1][1]] = '*'
    grid[l[1][0]][l[0][1]] = '*'
    for i in grid:
        print(''.join(i))