from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    def solve():
        n,m,k=rns()
        if m>n*(n-1)/2:
            return False
        if m<n-1:
            return False
        if k<2:
            return False
        if n==1:
            return m==0
        if m==n*(n-1)/2:
            return k>2
        return k>3

    YN(solve())