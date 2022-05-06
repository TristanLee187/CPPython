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
    if len(s)==1:
        print('Bob', ord(s)-96)
    else:
        su=sum([ord(c)-96 for c in s])
        if len(s)%2==0:
            print('Alice', su)
        else:
            last=min(ord(s[0]), ord(s[-1]))-96
            print('Alice', su-2*last)
