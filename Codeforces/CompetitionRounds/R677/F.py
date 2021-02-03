rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

n,m,k=rns()
l=[]
for i in range(n):
    l.append(rl())
ans=0
for i in l:
    ans+=sum(sorted(i, reverse=True)[:m//2])
ans=ans//k*k
print(ans)
