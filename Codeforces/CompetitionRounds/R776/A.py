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
    s=rs()
    c=rs()
    def solve():
        if c not in s:
            return False
        a=[i for i in range(len(s)) if s[i]==c]
        for index in a:
            if index%2==(len(s)-index-1)%2==0:
                return True
        return False
    YN(solve())
