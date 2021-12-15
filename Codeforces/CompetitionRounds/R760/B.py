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
    strs=rs().split()
    ans=strs[0]
    for i in range(1,n-2):
        if strs[i][0]!=ans[-1]:
            ans+=strs[i][0]
        ans+=strs[i][1]
    if len(ans)<n:
        ans+='a'
    print(ans)