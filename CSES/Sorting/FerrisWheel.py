rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,x=rns()
p=rl()
p.sort()
ans=0
i=0
j=n-1
while i<=j:
    if i==j:
        ans+=1
        break
    else:
        if p[i]+p[j]>x:
            ans+=1
            j-=1
        else:
            ans+=1
            j-=1
            i+=1
print(ans)