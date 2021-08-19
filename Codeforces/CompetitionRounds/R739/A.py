from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

a=[]
for i in range(1667):
    if i%3!=0 and i%10!=3:
        a.append(i)
for _ in range(rn()):
    k=rn()
    print(a[k-1])
