from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

for _ in range(rn()):
    a,b,k=rns()
    if a==b:
        low=0
    elif max(a,b)%min(a,b)==0:
        low=1
    else:
        low=2
    def primefact(x):
        ans=defaultdict(int)
        flag=False
        i=2
        s=int(x**0.5)+1
        while i<s:
            if x%i==0:
                flag=True
                ans[i]+=1
                rest=primefact(x//i)
                for num in rest:
                    ans[num]+=rest[num]
                break
            i+=1+(i&1)
        if not flag and x!=1:
            ans[x]=1
        return ans
    ap=primefact(a)
    bp=primefact(b)
    ea=sum([ap[i] for i in ap])
    eb=sum([bp[i] for i in bp])
    high=ea+eb
    YN(low<=k<=high and (k!=1 or (k==1 and low==1)))