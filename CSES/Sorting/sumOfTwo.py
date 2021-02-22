rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,x=rns()
l=rl()
a=[]
for i in range(n):
    a.append([l[i],i+1])
a.sort()
i=0
j=n-1
ans=[-1,-1]
while i<j:
    if a[i][0]+a[j][0]==x:
        ans=[a[i][1],a[j][1]]
        break
    elif a[i][0]+a[j][0]>x:
        j-=1
    else:
        i+=1
if ans!=[-1,-1]:
    print(ans[0],ans[1])
else:
    print('IMPOSSIBLE')