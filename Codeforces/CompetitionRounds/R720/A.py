from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b=rns()
    if b==1:
        print('NO')
    else:
        print('YES')
        b*=2
        x=a*(b-1)
        y=a
        z=a*b
        print(x,y,z)