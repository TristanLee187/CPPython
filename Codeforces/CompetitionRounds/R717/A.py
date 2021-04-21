from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    a=rl()
    i=0
    j=0
    while j<k:
        if a[i]>0:
            a[i]-=1
            a[-1]+=1
            j+=1
        elif i==n-1:
            break
        else:
            i+=1
    print(*a)