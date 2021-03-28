rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

h,w,x,y=rns()
x-=1
y-=1
grid=[]
for i in range(h):
    grid.append(rs())
ans=0
for i in range(x, h):
    if grid[i][y]=='#':
        break
    else:
        ans+=1

for i in range(x-1,-1,-1):
    if grid[i][y]=='#':
        break
    else:
        ans+=1

for i in range(y+1,w):
    if grid[x][i]=='#':
        break
    else:
        ans+=1

for i in range(y-1,-1,-1):
    if grid[x][i]=='#':
        break
    else:
        ans+=1

print(ans)