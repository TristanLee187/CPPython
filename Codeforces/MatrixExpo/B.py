from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


def matrix_mult(a,b):
    n=len(b)
    m=len(a[0])
    ans=[[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(n):
                ans[i][j]+=a[k][j]*b[i][k]
                ans[i][j]%=mod
    return ans


n=rn()
ans=[[1,0],[0,1]]
m=[[19,6],[7,20]]
while n:
    if n&1:
        ans=matrix_mult(ans,m)
    m=matrix_mult(m,m)
    n//=2
print(ans[0][0])
