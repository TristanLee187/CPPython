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
    a=rl()
    def solve():
        if n==1:
            return True
        x,y=0,n-1
        while x<y and a[x]==a[y]:
            x+=1
            y-=1
        if x>=y:
            return True
        b=[i for i in a if i!=a[x]]
        c=[i for i in a if i!=a[y]]
        return b==b[::-1] or c[::-1]==c
    YN(solve())