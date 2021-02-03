from decimal import *

t=int(input())
for i in range(t):
    n,k=map(int, input().split(' '))
    l=list(map(int, input().split(' ')))
    
    for i in range(n):
        if l[i]%k==0:
            l[i]=0
        else:
            l[i]=k-(l[i]%k)
    l=sorted(l)
    ans=Decimal(0)
    count=1
    for i in range(1, n):
        if l[i]==l[i-1] and l[i]!=0:
            ans = Decimal(max(ans, Decimal(l[i]+Decimal(count)*Decimal(k))))
            count+=1
        else:
            ans=Decimal(max(ans, l[i]))
            count=1
    if n==1:
        if l[0]==0:
            print(0)
        else:
            print(l[0]+1)
    elif ans==0:
        print(0)
    else:
        print(ans+Decimal(1))
