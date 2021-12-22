from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=set()
    for i in range(1,10**5):
        if i**2>n:
            break
        if i**2<=n:
            s.add(i**2)
        if i**3<=n:
            s.add(i**3)

    print(len(s))