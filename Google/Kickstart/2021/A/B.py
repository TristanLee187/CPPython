rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    ans = 0
    r,c=rns()
    grid=[]
    for i in range(r):
        grid.append(rs().split())

    def comp(row):
        c=len(row)
        indexes=[i for i in range(c) if row[i]=='1']
        ans=c*[0]
        for i in range(len(indexes)):
            if i==0:
                ans[indexes[i]]=1
            else:
                ans[indexes[i]] = ans[indexes[i]-1]+1
        for i in range(c-1,0,-1):
            if ans[i]>0 and ans[i-1]>0:
                ans[i-1]=ans[i]
        return ans

    def solve(r,c,grid):
        ans=0
        pre=c*[0]
        for i in range(r):
            ones = []
            for j in range(c):
                if grid[i][j]=='1':
                    pre[j]+=1
                    ones.append(j)
                else:
                    pre[j]=0
            groups=comp(grid[i])
            curr=-1
            for j in range(c):
                if groups[j]>0:
                    curr+=1
                    ans += max(min(pre[j]//2-1, groups[j]-curr-1),0)
                    ans+=max(min(pre[j]//2-1, curr),0)
                else:
                    curr=-1
        return ans

    def rotate(grid):
        ans=[]
        for i in range(len(grid[0])):
            ans.append([grid[j][i] for j in range(len(grid)-1,-1,-1)])
        return ans

    for i in range(4):
        ans+=solve(r,c,grid)
        grid=rotate(grid)
        r,c=c,r
    print('Case #' + str(_ + 1) + ': ' + str(ans))