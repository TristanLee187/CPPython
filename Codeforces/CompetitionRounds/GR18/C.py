from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rs()
    b=rs()
    one0=0
    zero1=0
    solved1=0
    solved0=0
    for i in range(n):
        if a[i]!=b[i]:
            if a[i]=='1':
                one0+=1
            else:
                zero1+=1
        elif a[i]=='1':
            solved1+=1
        else:
            solved0+=1
    ans=float('inf')
    if solved1==1 and one0+zero1+1==n:
        ans=1
    if solved1>0 and (solved1+solved0)%2==1 and solved1==solved0+1:
        ans=min(ans,solved1+solved0)
    if one0==zero1:
        ans=min(ans,2*zero1)
    if ans==float('inf'):
        print(-1)
    else:
        print(ans)