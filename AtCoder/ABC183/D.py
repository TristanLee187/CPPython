rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
n,w=rns()
l=[]
for i in range(n):
    l.append(rl())
l.sort()
ans=True
i=0
j=0
acc=0
while i<n:
    while j<n and l[j][0]<l[i][1]:
        acc+=l[j][2]
        j+=1
    if acc>w:
        print(i,j,acc)
        ans=False
        break
    acc-=l[i][2]
    i+=1
yn(ans)