rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
a=rl()
a=[[a[i],i+1] for i in range(n)]
a.sort()
i,j,k,l=0,1,n-2,n-1
while a[i][0]+a[l][0]!=a[k][0]+a[j][0] and j!=k:
    if a[i][0]+a[l][0]<a[k][0]+a[j][0]:
        i+=1
        j+=1
    else:
        k-=1
        l-=1
if a[i][0]+a[l][0]==a[k][0]+a[j][0] and j!=k:
    print('YES')
    print(*[a[c][1] for c in [i,l,k,j]])
else:
    print('NO')