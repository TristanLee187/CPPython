n=int(input())
hs=n//100
ans=0

ans += hs
n=n%100

ts = n//20

ans+=ts

n=n%20
tens=n//10
ans+=tens

n=n%10
fives=n//5
ans+=fives

n=n%5
ans+=n

print(ans)

