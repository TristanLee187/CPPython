from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    s=rs()
    f=rs()
    for i in s:
        d=float('inf')
        for j in f:
            d=min([d,abs(ord(i)-ord(j)),26-abs(ord(i)-ord(j))])
        ans+=d
    print('Case #' + str(_+1)+': ' + str(ans))