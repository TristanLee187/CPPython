rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
l=rl()
l.sort()
med=l[n//2]
ans=0
for i in l:
    ans+=abs(i-med)
print(ans)