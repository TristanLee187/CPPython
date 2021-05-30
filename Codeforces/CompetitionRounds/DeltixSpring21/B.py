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
    print(6*n//2)
    for i in range(0,n,2):
        print(1,i+1,i+2)
        print(2, i+1, i + 2)
        print(1, i+1, i + 2)
        print(2, i+1, i + 2)
        print(1, i+1, i + 2)
        print(2, i+1, i + 2)
