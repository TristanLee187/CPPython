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
    keys=rs()
    s=rs()
    ans=0
    for i in range(1,len(s)):
        ans+=abs(keys.index(s[i])-keys.index(s[i-1]))
    print(ans)