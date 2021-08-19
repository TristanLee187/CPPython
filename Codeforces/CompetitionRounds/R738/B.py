from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=list(rs())
    first=-1
    for i in range(n):
        if s[i]!='?':
            first=i
            break
    if first!=-1:
        if first%2==0:
            s[0]=s[first]
        else:
            i=['B','R'].index(s[first])
            s[0] = ['B','R'][not i]
    else:
        s[0]='B'
    for i in range(1,n):
        if s[i]=='?':
            j = ['B', 'R'].index(s[i-1])
            s[i] = ['B', 'R'][not j]
    print(''.join(s))
