from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b=rns()
    c=abs(a-b)
    if c==0:
        print(0,0)
    else:
        print(c, min((c-a%c)%c, a%c))