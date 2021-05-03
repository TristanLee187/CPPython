from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter

for _ in range(rn()):
    n,l,r=rns()
    c=rl()
    lefts = Counter(c[:l])
    rights = Counter(c[l:])
    for i in lefts:
        if i in rights:
            m=min(lefts[i],rights[i])
            lefts[i]-=m
            rights[i]-=m
            l-=m
            r-=m

    ans=0
    ans+=min(l,r)
    l-=ans
    r-=ans
    if l>0:
        for i in lefts:
            ans+=min(l//2,lefts[i]//2)
            l-=lefts[i]//2*2
            if l<=0:
                break
        if l>0:
            ans+=l
    if r>0:
        for i in rights:
            ans+=min(r//2,rights[i]//2)
            r-=rights[i]//2*2
            if r<=0:
                break
        if r>0:
            ans+=r

    print(ans)
