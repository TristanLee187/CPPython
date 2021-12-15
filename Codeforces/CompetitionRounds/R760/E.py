from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    b=rl()
    ans=[]
    def solve(arr):
        if sum(b)%(n*(n+1)//2)!=0:
            return False
        s=sum(b)//(n*(n+1)//2)
        for i in range(n):
            diff=b[i]-b[i-1]
            if (s-diff)%n!=0 or (s-diff)<=0:
                return False
            arr.append((s-diff)//n)
        return True
    yn=solve(ans)
    if yn:
        print('YES')
        print(*ans)
    else:
        print('NO')