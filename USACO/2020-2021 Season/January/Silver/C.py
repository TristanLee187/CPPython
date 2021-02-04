n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split())))
ans=0
for i in range(n):
    total=0
    even=0
    for j in range(n):
        total+=grid[i][j]
        if j%2==0:
            even+=grid[i][j]
    ans+=max(even,total-even)

tans=0
for i in range(n):
    col=[grid[j][i] for j in range(n)]
    total=0
    even=0
    for j in range(n):
        total+=col[j]
        if j%2==0:
            even+=col[j]
    tans+=max(even,total-even)

print(max(ans,tans))