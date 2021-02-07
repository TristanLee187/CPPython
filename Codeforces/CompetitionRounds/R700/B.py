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
    from math import ceil
    A,B,n=rns()
    a=rl()
    b=rl()
    c=[[a[i],b[i]] for i in range(n)]
    c.sort()
    ans=True
    for i in range(n):
        B-=c[i][0]*ceil(c[i][1]/A)
        if B<=0:
            if B+c[i][0]>=1:
                ans=(i==n-1)
            else:
                ans=False
            break
    YN(ans)