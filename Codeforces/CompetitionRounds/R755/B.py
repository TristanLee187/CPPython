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
    n,m=rns()
    ans=n*(m//3)
    ans+=(m%3)*(n//3)
    a=sorted([n%3,m%3])
    if a==[1,1]:
        ans+=1
    elif a==[1,2]:
        ans+=1
    elif a==[2,2]:
        ans+=2
    print(ans)
