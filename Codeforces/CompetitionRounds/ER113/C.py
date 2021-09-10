from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=998244353
from itertools import accumulate

for _ in range(rn()):
    n=rn()
    a=rl()
    a.sort()
    ans=0
    def fact(n):
        ans=1
        for i in range(2,n+1):
            ans*=i
            ans%=mod
        return ans
    if a[-1]>a[-2]+1:
        pass
    else:
        t=a.count(a[-2])
        s=n-t
        ss=fact(s)
        ans=(t*fact(n-1))%mod
        print(ans)
        sss=[1]
        for i in range(s,0,-1):
            sss.append(sss[-1]*i)
            sss[-1]%=mod
        sss.reverse()
        start=n-s
        for i in range(n-s-1):
            sss[i]*=start
            sss[i]%=mod
            start*=start+1
            start%=mod
        sss.reverse()
        ssss=list(accumulate(sss))
        for i in range(t,n):
            r=n-i-1
            ans+=3*ssss[r]
            ans%=mod
    print(ans)