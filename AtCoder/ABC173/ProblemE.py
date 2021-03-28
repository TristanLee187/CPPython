from decimal import *

n,k=map(int,input().split(' '))
l=list(map(int, input().split(' ')))
l=sorted(l)

ans=Decimal(1)

if n==1:
    print(l[0])
elif k==n:
    for i in l:
        ans*=i
    ans=ans%(10**9+7)
    print(ans)
elif l[1]>=0:
    for i range(n-k,n):
        ans*=l[i]
    ans=ans%(10**9+7)
    print(ans)
else:
    while k>0:
        a=l[0]*l[-1]
        b=l[-1]
        if a>b:
            
    


    
    
