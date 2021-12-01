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
    x1,p1=rns()
    x2,p2=rns()
    x1=str(x1)
    x2=str(x2)
    if len(x1)+p1<len(x2)+p2:
        print('<')
    elif len(x1)+p1>len(x2)+p2:
        print('>')
    else:
        def solve():
            for i in range(max(len(x1),len(x2))):
                a=x1[i] if i<len(x1) else '0'
                b=x2[i] if i<len(x2) else '0'
                if a>b:
                    return '>'
                if a<b:
                    return '<'
            return '='
        print(solve())

