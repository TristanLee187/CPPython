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
    s=rs()
    bal=0
    first=0
    ans=0
    left=n
    possgood=True
    for i in range(n):
        if s[i]=='(':
            bal+=1
        else:
            bal-=1
        if bal==0 and possgood:
            ans+=1
            left-=i-first+1
            first=i+1
        elif s[i]==s[first] and i!=first:
            ans+=1
            left-=i-first+1
            first=i+1
            possgood=True
            bal=0
        elif bal<0:
            possgood = False
    print(ans, left)