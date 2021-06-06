from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a=rl()
    a1=a[:2]
    a2=a[2:]
    b=sorted(a)
    ans = (b[-1] in a1 and b[-2] in a2) or (b[-1] in a2 and b[-2] in a1)
    YN(ans)