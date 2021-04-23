from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


def pans(ans):
    for i in range(n):
        print(*ans[i][:i + 1])


n=rn()
p=rl()
ans=[n*[0] for i in range(n)]
for i in range(n):
    ans[i][i] = p[i]
for i in range(n):
    x=i
    y=i
    for j in range(p[i]-1):
        if x==0 or ans[y][x-1]!=0:
            y+=1
        else:
            x-=1
        ans[y][x] = p[i]
pans(ans)