from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    a=list(map(lambda x:x%2, a))
    b=[i for i in range(n) if a[i]==0]
    def t(indeces,tr):
        if len(indeces)!=len(tr):
            return float('inf')
        ans=0
        for i in range(len(indeces)):
            ans+=abs(indeces[i]-tr[i])
        return ans
    pans=float('inf')
    pans=min(pans, t(b,range(0,n,2)),t(b,range(1,n,2)))
    if pans==float('inf'):
        print(-1)
    else:
        print(pans)
