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
    l=rl()
    i=l.index(min(l))
    print(n-1)
    for j in range(i+1,n):
        print(i+1,j+1,l[i],l[i] + (1 if (j-i)%2==1 else 0))
    for j in range(i):
        print(i+1, j+1, l[i], l[i] + (1 if (i - j) % 2 == 1 else 0))