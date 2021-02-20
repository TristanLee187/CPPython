rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

h,w=rns()
grid=[]
for i in range(h):
    grid.append(rs())
ans=0
for row in range(h-1):
    for col in range(w-1):
        minigrid=[grid[row][col],grid[row+1][col],grid[row][col+1],grid[row+1][col+1]]
        ans += minigrid.count('#')%2
print(ans)