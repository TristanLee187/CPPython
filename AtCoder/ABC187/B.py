rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
p=[]
for i in range(n):
    p.append(rl())
ans=0
for i in range(n):
    for j in range(i+1,n):
        rise=p[j][1]-p[i][1]
        run=p[j][0]-p[i][0]
        if run!=0 and -1<=rise/run<=1:
            ans+=1
print(ans)