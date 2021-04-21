from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7


def f(nums):
    dp = [[-1] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

    def ssum(arr, k, n):
        if n == 0:
            if k > 0:
                return False
            else:
                return True
        if dp[n][k] == -1:
            if arr[n - 1] <= k:
                dp[n][k] = ssum(arr, k - arr[n - 1], n - 1) or ssum(arr, k, n - 1)
            else:
                dp[n][k] = ssum(arr, k, n - 1)

        return dp[n][k]

    return ssum(nums, sum(nums) // 2, len(nums)) if sum(nums) % 2 == 0 else False

n=rn()
a=rl()
half=sum(a)/2
if half%1!=0:
    print(0)
else:
    if f(a):
        ans=0
        for i in a:
            if i%2==1:
                ans=i
                break
        if ans==0:
            for i in a:
                if i//2%2==1:
                    ans=i
                    break
        if ans==0:
            ans=min(a)

        print(1)
        print(a.index(ans)+1)
    else:
        print(0)