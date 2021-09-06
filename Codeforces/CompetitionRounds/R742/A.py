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
    s=rs()
    ans=[]
    i=0
    while i<n:
        if s[i]=='U':
            ans.append('D')
        elif s[i]=='D':
            ans.append('U')
        else:
            ans+=['L','R']
            i+=1
        i+=1
    print(''.join(ans))
