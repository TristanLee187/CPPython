from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    a=s.count('A')
    b=s.count('B')
    c=s.count('C')
    def solve(a,b,c):
        if a>b:
            return False
        if c>b:
            return False
        return b==a+c
    YN(solve(a,b,c))