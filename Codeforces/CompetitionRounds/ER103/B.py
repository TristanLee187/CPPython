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
    from math import ceil
    n,k=rns()
    l=rl()
    ans=0
    pre=l[0]
    for i in range(1,n):
        if l[i]*100>k*pre:
            ans+=ceil((l[i]*100-k*pre)/k)
            pre+=ceil((l[i]*100-k*pre)/k)
        pre+=l[i]
    print(ans)