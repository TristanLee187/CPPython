rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from itertools import accumulate

def pre(a):
    return list(accumulate(a,lambda a,b:(a+b)%mod))

def suff(a):
    return list(reversed(list(accumulate(a[::-1],lambda a,b:(a+b)%mod))))

for _ in range(rn()):
    n,k=rns()
    ans=1
    nums = (n-1)*[1]
    for i in range(k-1):
        ans+=sum(nums)
        if i%2==0:
            nums = suff(nums)
        else:
            nums=pre(nums)
        ans%=mod
    if k>1:
        ans+=1
        ans%=mod
    print(ans)