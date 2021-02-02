from decimal import *

l=list(map(int, input().split(' ')))
a=l[0]
v=l[1]
l=list(map(int, input().split(' ')))
b=l[0]
w=l[1]
s=int(input())
ans=True
if a>b:
    ans=Decimal(a)-Decimal(v*s)<=Decimal(b)-Decimal(w*s)
else:
    ans=Decimal(a)+Decimal(v*s)>=Decimal(b)+Decimal(w*s)
if ans:
    print("YES")
else:
    print("NO")
    
