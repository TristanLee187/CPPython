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
    n,a,b=rns()
    def solve():
        if n==2:
            return [a,b]
        nums=[i for i in range(1,n+1) if i not in [a,b]]
        first = nums[:len(nums)//2]
        second = nums[len(nums)//2:]
        if a>second[0] or b<first[-1]:
            return [-1]
        return [a]+second+[b]+first
    print(*solve())

