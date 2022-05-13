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
    a,b,c,d=rns()
    def inter(A,B,C,D):
        for i in range(1,51):
            if A<=i<=B and C<=i<=D:
                return True
        return False
    if inter(a,b,c,d):
        print(max(a,c))
    else:
        print(a+c)