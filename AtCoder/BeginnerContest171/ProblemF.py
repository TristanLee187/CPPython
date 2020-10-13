from decimal import *

k=int(input())
count=0
s=len(input())
ans=Decimal(1)
while count<k:
    count+=1
    ans = ans*(s+1)*26
    ans = ans%(10**9+7)
    s+=1
print(ans)
    
    
    
