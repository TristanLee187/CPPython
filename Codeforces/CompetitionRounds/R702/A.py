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

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=0
    for i in range(n-1):
        if abs(l[i]-l[i+1])>min(l[i],l[i+1]):
            a=min(l[i],l[i+1])
            while a<max(l[i],l[i+1]):
                ans+=1
                a*=2
            ans-=1
    print(ans)