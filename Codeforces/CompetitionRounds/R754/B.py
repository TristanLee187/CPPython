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
    s=rs()
    a=[i for i in range(n) if s[i]=='1']
    aa=len(a)
    b=[]
    for i in range(n-1,-1,-1):
        if aa==0:
            break
        elif s[i]=='0':
            aa-=1
            b.append(i)
        else:
            aa-=1
            a.pop()
    if len(a)==0 and len(b)==0:
        print(0)
    else:
        print(1)
        b.reverse()
        c=a+b
        print(len(c), *[i+1 for i in c])