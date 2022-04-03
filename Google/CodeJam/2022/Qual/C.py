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
    n=rn()
    a=rl()
    a.sort()
    curr=1
    for i in range(n):
        if a[i]>=curr:
            ans+=1
            curr+=1
    print('Case #' + str(_+1)+': ' + str(ans))