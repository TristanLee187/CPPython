rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
for _ in range(rn()):
    a,b=rns()
    ans=0
    d=b
    if b==1:
        d=2
        ans+=1
    c=a
    while c>0:
        c=c//d
        ans+=1
    for i in range(b,int(a**0.5)+1):
        if i!=1:
            tans=i-b
            c=a
            while c>0:
                c=c//i
                tans+=1
            ans=min(ans,tans)
    print(ans)