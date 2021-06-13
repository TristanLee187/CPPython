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
    r1=rl()
    r2=rl()
    in1={r1[i]:i for i in range(n)}
    in2 = {r2[i]: i for i in range(n)}
    c=0
    seen=[False for i in range(n)]
    for i in range(n):
        if not seen[i]:
            seen[i]=True
            a=-1
            j=i
            while a!=r1[i]:
                j=in1[r2[j]]
                a=r1[j]
                seen[j]=True
            c+=1
    print(pow(2,c,mod))
