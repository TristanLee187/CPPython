rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,x=rns()
x*=100
l=[]
for i in range(n):
    l.append(rl())
acc=0
ans=0
for i in range(n):
    acc+=l[i][0]*l[i][1]
    ans+=1
    if acc>x:
        break
if acc<=x:
    ans=-1
print(ans)