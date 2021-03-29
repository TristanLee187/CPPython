rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

n,m=rns()
ops=[]
for i in range(n):
    op=rl()
    op[1] /= 10**5
    ops.append(op)
