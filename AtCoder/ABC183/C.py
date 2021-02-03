rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
from itertools import permutations

n,k=rns()
l=[]
for i in range(n):
    l.append(rl())
a=permutations(list(range(1,n)))
ans=0
for i in a:
    b=[0]+list(i)+[0]
    s=0
    for i in range(n):
        s+=l[b[i]][b[i+1]]
    if s==k:
        ans+=1
print(ans)