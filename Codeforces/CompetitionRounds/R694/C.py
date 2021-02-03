rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
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
    n,m=rns()
    k=rl()
    c=rl()
    d={}
    for i in range(m):
        d[i]=0
    for i in k:
        d[i-1]+=1
    ans=0
    count=0
    for i in d:
        if count>=n:
            break
        add=min(n-count,d[i]+1)
        ans+=add*c[i]
        count+=add
    print(ans)
    print(d)