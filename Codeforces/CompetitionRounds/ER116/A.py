from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=list(rs())
    ss=[s[0]]
    for i in s[1:]:
        if i!=ss[-1]:
            ss.append(i)
    a=ss.count('a')
    b=ss.count('b')
    if a==b:
        s[0] = 'a' if s[0]=='b' else 'b'
    print(''.join(s))