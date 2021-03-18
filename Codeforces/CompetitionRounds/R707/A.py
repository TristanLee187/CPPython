rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
import math
for _ in range(rn()):
    n=rn()
    a=[]
    b=[]
    for i in range(n):
        c,d=rns()
        a.append(c)
        b.append(d)
    t=rl()
    ans=a[0]+t[0]
    for i in range(n-1):
        ans=max(b[i],ans+math.ceil((b[i]-a[i])/2))
        ans+=a[i+1]-b[i]+t[i+1]
    print(ans)