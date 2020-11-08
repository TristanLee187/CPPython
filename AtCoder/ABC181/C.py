rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

n=rn()
l=[]
for i in range(n):
    l.append(rl())
ans=False
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            def isCol(a,b,c):
                area=a[0]*b[1]+b[0]*c[1]+c[0]*a[1]
                area-=a[1]*b[0]+b[1]*c[0]+c[1]*a[0]
                return area==0
            if isCol(l[i],l[j],l[k]) and (l[i]!=l[j]!=l[k]):
                ans=True
                break


yn(ans)