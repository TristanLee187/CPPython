rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    m0=-1
    m1=-1
    for i in range(len(s)):
        if s[i]=='0':
            m0=i
        if s[i]=='1':
            m1=i
    ans = True
    if m1!=-1 and m0!=-1:
        for i in range(len(s)-2):
            if s[i]=='1' and i<m0 and i!=m1 and s[i+2]=='0' and i+2!=m0:
                ans=False
                break
    YN(ans)