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
    s=rs()
    ans=True
    keys=[]
    for i in range(6):
        if s[i].lower() == s[i]:
            keys.append(s[i])
        elif s[i].lower() in keys:
            pass
        else:
            ans=False
    YN(ans)