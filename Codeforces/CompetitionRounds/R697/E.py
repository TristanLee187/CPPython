rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

from math import comb
for _ in range(rn()):
    n,k=rns()
    a=rl()
    a.sort()
    num=a[n-k]
    count=1
    while n-k+count<n and a[n-k+count]==num:
        count+=1
    ans=comb(a.count(num),count)
    print(mod(ans))