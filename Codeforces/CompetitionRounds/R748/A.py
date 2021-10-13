from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b,c=rns()
    ans=[]
    ans.append(max([0,b-a+1,c-a+1]))
    ans.append(max([0,a-b+1,c-b+1]))
    ans.append(max([0,b-c+1,a-c+1]))
    print(*ans)