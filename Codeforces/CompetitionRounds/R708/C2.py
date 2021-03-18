rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    def solve(n):
        if n==4:
            return [1,1,2]
        elif n%2==1:
            return [1,n//2,n//2]
        return list(map(lambda x:2*x, solve(n//2)))
    ans = (k-3)*[1] + solve(n-k+3)
    print(*ans)