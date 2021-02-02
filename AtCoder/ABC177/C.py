n=int(input())
l=list(map(int,input().split()))
mod=10**9+7
pre=sum(l)
ans=0
for i in l:
    pre-=i
    ans+=i*pre
    ans%=mod
print(ans)