from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    if a==sorted(a):
        print(0)
    elif a[0]==1 or a[-1]==n:
        print(1)
    elif a[0]==2 or a[-1]!=1 or a[-1]==n-1 or a[0]!=n:
        print(2)
    else:
        print(3)