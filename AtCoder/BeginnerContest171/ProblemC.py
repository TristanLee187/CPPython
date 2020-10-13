from decimal import *

n=Decimal(input())
chars=['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
ans=''
while n>0:
    r=n%26
    ans = chars[int(r)]+ans
    if r==0:
        n = n//26-1
    else:
        n=n//26

print(ans)
