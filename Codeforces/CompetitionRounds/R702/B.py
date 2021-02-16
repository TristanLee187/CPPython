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
    rems=[0,0,0]
    for i in l:
        rems[i%3]+=1
    give=[i-n//3 for i in rems]
    c=len([i for i in give if i>0])
    ans=0
    if c==1:
        i=give.index(max(give))
        ans+=abs(give[(i+1)%3])
        ans+=2*abs(give[(i+2)%3])
    elif c==2:
        i=give.index(min(give))
        ans+=give[(i-1)%3]
        ans+=2*give[(i-2)%3]
    print(ans)