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
    w,l=rns()
    bot=rl()[1:]
    top=rl()[1:]
    left=rl()[1:]
    right=rl()[1:]
    def maxdiff(arr):
        return arr[-1]-arr[0]
    ans=max(maxdiff(bot),maxdiff(top))*l
    ans=max(ans, max(maxdiff(left),maxdiff(right))*w)
    print(ans)
