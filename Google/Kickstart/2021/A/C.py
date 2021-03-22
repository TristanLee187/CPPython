rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)
import heapq

for _ in range(rn()):
    ans = 0
    r,c=rns()
    grid=[]
    m=float('inf')
    for i in range(r):
        grid.append(rl())
        m=min(m,min(grid[-1]))
    d={}
    p=set()
    for i in range(r):
        for j in range(c):
            p.add((i,j))
            if grid[i][j] not in d:
                d[grid[i][j]]=set()
            d[grid[i][j]].add((i,j))
    h=[]
    for i in d:
        heapq.heappush(h,[-i,d[i]])

    add={}
    while len(h)>0 and len(p)>0:
        val = heapq.heappop(h)
        val[0]=-val[0]
        if val[0]<m:
            break
        if val[0]-1 not in add:
            add[val[0]-1]=set()
        if val[0] in add:
            val[1] = val[1] | add[val[0]]
        num=val[0]
        for i,j in val[1]:
            if (i,j) in p:
                p.remove((i,j))
            if i+1<r and num-1>grid[i+1][j]:
                ans+=num-1-grid[i+1][j]
                grid[i+1][j]=num-1
                add[num-1].add((i+1,j))
            if j+1<c and num-1>grid[i][j+1]:
                ans+=num-1-grid[i][j+1]
                grid[i][j+1]=num-1
                add[num-1].add((i,j+1))
            if i-1>=0 and num-1>grid[i-1][j]:
                ans+=num-1-grid[i-1][j]
                grid[i-1][j]=num-1
                add[num-1].add((i-1,j))
            if j-1>=0 and num-1>grid[i][j-1]:
                ans+=num-1-grid[i][j-1]
                grid[i][j-1]=num-1
                add[num-1].add((i,j-1))
        if num-1 not in d:
            heapq.heappush(h,[-num+1,add[num-1]])


    print('Case #' + str(_ + 1) + ': ' + str(ans))