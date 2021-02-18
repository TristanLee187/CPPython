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
    ans=True
    for i in range(n-1):
        if l[i]<i:
            ans=False
            break
        l[i+1]+=l[i]-(i)
        l[i]=(i)
    if n>1:
        ans=ans and l[-1]>l[-2]
    YN(ans)