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

from itertools import accumulate
n,q,k=rns()
a=rl()
qs=[]
for i in range(q):
    qs.append(rl())
ls=[1]
for i in range(1,n-1):
    ls.append(a[i+1]-a[i-1]-2)
ls.append(1)
pre=list(accumulate(ls))
for query in qs:
    l=query[0]-1
    r=query[1]-1
    if l==r:
        print(k-1)
    else:
        ans=1
        if l==0:
            ans=a[1]-2
        else:
            ans=a[l+1]-2
        ans+=pre[r-1]-pre[l]
        ans+=k-a[r-1]-1
        print(ans)

