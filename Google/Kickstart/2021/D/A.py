from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

for _ in range(rn()):
    ans=0
    row1=rl()
    row2=rl()
    row2.insert(1,-1)
    row3=rl()

    def f(d):
        diff=[d[i]-d[i-1] for i in range(1,3)]
        return diff[0]==diff[1]

    ans+=f(row1)
    ans+=f(row3)
    ans+=f([row1[0], row2[0], row3[0]])
    ans += f([row1[2], row2[2], row3[2]])

    d=defaultdict(int)

    def add(a,b):
        a,b=sorted([a,b])
        if a%2==b%2:
            d[(b+a)//2]+=1

    add(row1[0], row3[2])
    add(row1[1], row3[1])
    add(row1[2], row3[0])
    add(row2[0], row2[2])

    ans+=max(d.values()) if d.values() else 0
    print('Case #' + str(_+1)+': ' + str(ans))
