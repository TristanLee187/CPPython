from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import gcd

n=rn()
nums=[]
for i in range(1,n):
    if gcd(i,n)==1:
        nums.append(i)
prod=1
for num in nums:
    prod*=num
    prod%=n
if prod!=1:
    nums.remove(prod)
ans=len(nums)

print(ans)
print(*nums)