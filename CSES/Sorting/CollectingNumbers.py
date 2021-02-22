rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
l=rl()
a=[]
for i in range(n):
    a.append([l[i],i])
a.sort()
ans=1
for i in range(1,n):
    if a[i][1]<a[i-1][1]:
        ans+=1
print(ans)