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
    ans=9*(len(str(n))-1)
    for i in range(1,10):
        test = int(len(str(n))*str(i))
        if n>=test:
            ans+=1
    print(ans)