rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

n,k=rns()
l=rl()
a=(n+1)*[0]
for i in l:
    a[i]+=1
ans=0
m=float('inf')
for i in range(n+1):
    if a[i]==0:
        break
    m=min(m,a[i])
    ans+=min(k,a[i],m)
print(ans)