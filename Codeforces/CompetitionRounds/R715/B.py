from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    if s.count('T')==2*s.count('M'):
        bal=0
        ans=True
        for i in s:
            if i=='T':
                bal+=1
            else:
                bal-=1
            if bal<0:
                ans=False
                break
        YN(ans)
    else:
        print('NO')