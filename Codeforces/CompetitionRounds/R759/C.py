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
    n,k=rns()
    x=rl()
    x.sort()
    neg=[i for i in x if i<0]
    pos=[i for i in x if i>0]
    a=len(neg)
    b=len(pos)
    neg.reverse()
    mins=[0,0]
    if a>0:
        mins[0]=-neg[-1]
    if b>0:
        mins[1]=pos[-1]
    def solve(arr,k):
        if not arr:
            return 0
        ends=[]
        while arr:
            app=arr[-1]
            for i in range(min(k,len(arr))):
                arr.pop()
            ends.append(app)
        pans=2*abs(sum(ends))-abs(ends[0])
        return pans
    ans=solve(pos,k)+solve(neg,k)
    ans+=min(mins)
    print(ans)
