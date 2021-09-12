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
    c=0
    for i in range(len(s)-1):
        if s[i]=='0' and s[i+1]=='1':
            c+=1
    if s[-1]=='0':
        c+=1
    print(min(c,2))
