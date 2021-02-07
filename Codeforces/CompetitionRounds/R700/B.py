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
    c.sort(key=lambda x:x[0])
    a=[c[i][0] for i in range(n)]
    b=[c[i][1] for i in range(n)]
    ans=True
    for i in range(n):
        B-=a[i]*ceil(b[i]/A)
        if B<=0:
            if B+a[i]>=1:
                ans=(i==n-1)
            else:
                ans=False
            break
    c = [[a[i], b[i]] for i in range(n)]
    c.sort(key=lambda x: x[1])
    a = [c[i][0] for i in range(n)]
    b = [c[i][1] for i in range(n)]
    pans = True
    for i in range(n):
        B -= a[i] * ceil(b[i] / A)
        if B <= 0:
            if B + a[i] >= 1:
                pans = (i == n - 1)
            else:
                pans = False
            break
    YN(ans or pans)