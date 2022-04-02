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
    x,y=rns()
    def solve():
        if x==y==0:
            return 0
        if (x**2+y**2)**0.5 == int((x**2+y**2)**0.5):
            return 1
        return 2
    print(solve())