from decimal import *

def numFactors(n):
    ans=0
    for i in range(1, int(n**0.5+1)):
        if i==n**0.5:
            ans+=1
        elif n%i==0:
            ans+=2
    return ans


ans=Decimal(0)

for i in range(1, int(input())+1):
    ans += Decimal(i*numFactors(i))

print(ans)
    
