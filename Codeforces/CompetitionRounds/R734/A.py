from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    if n%3==0:
        print(n//3, n//3)
    elif n%3==1:
        print(n // 3+1, n // 3)
    else:
        print(n // 3, n // 3+1)