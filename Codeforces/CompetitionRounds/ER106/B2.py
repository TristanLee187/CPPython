rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    a=-1
    b=float('inf')
    for i in range(len(s)-1):
        if s[i:i+2]=='00':
            a=i
        if s[i:i+2]=='11':
            b=min(b,i)
    YN(a<b)