from sys import stdin
from math import gcd

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7


def gcd_l(a):
    if all([i==0 for i in a]):
        return -1
    ans = a[0]
    for num in range(1, len(a)):
        ans = gcd(ans, a[num])
    return ans


for _ in range(rn()):
    n = rn()
    a = rl()
    diff = [a[i] - a[i - 1] for i in range(1, n)]
    print(diff)
    ans=0
    for start in range(n//2+1):
        nums = diff[start:start+n // 2 - 1]
        g = gcd_l(nums)
        for i in range(start+n // 2 - 1, n-1):
            for j in range(n // 2 - 1):
                new_nums = nums.copy()
                new_nums.pop(j)
                new_nums.append(diff[i])
                g0 = gcd_l(new_nums)
                # print(g0)
                if g0==-1:
                    g=-1
                    break
                if g0 > g:
                    g = g0
                    nums = new_nums
            if g==-1:
                break
            ans=max(ans,g)
        if ans==-1:
            break
    print(ans)
