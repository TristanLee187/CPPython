rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

n=rn()
a=rl()
ans=0
pre=[]
s=set()
for num in a:
    s.add(num)
    pre.append(len(s))
s.clear()
suff=n*[0]
for i in range(n-1,-1,-1):
    s.add(a[i])
    suff[i]=len(s)

d=defaultdict(list)
for i in range(n):
    d[a[i]].append(i)

pointers = {key:0 for key in d.keys()}
for i in range(n):
    num = a[i]
    add=0
    p=pointers[num]
    if p+1>=len(d[num]):
        add = len(set(a[i:]))-1
    else:
        add = len(set(a[i:d[num][p+1]]))-1
        pointers[num]+=1
    ans+=add
print(ans)