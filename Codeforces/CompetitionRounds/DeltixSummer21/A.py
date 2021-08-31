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
    if abs(a-b)%2==1:
        print(-1)
    elif a==b==0:
        print(0)
    elif a==b:
        print(1)
    else:
        print(2)
