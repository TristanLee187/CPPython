rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

from math import ceil
for _ in range(rn()):
    n,k=rns()
    if n%2==0:
        if k%n==0:
            print(n)
        else:
            print(k%n)
    else:
        ans=0
        if k%n==0:
            ans=n
        else:
            ans=k%n
        if k>=ceil(n/2):
            a=ceil(n/2)
            b=n//2
            k-=a
            ans+=1
            ans+=k//b
        if ans%n==0:
            print(n)
        else:
            print(ans%n)