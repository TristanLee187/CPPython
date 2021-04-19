from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
ans=1
pans=[1]
nums=[]
for i in range(2,n):
    try:
        inv=pow(i,-1,n)
        nums.append((i,inv))
    except:
        ans+=0
prod=1
for i in nums:
    prod*=i[0]

for i in nums:
    if (prod/i[0])%i[1]==n%i[0]:
        ans+=1
        pans.append(i[0])
print(nums)
print(ans)
print(*pans)