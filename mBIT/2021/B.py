from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,m=rns()
if n>9*m or n==0 and m>1:
    print(-1)
else:
    ans=m*[0]
    for i in range(m):
        add=min(9,n)
        ans[i]+=add
        n-=add
    print(''.join(list(map(str,ans))))