from sys import stdin
from collections import defaultdict

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
ceil_div = lambda a, b: -(-a // b)
mod = 10 ** 9 + 7


def sieve(n, choice):
    ans = (n + 1) * [True]
    for i in range(2, int(n ** 0.5) + 1):
        if ans[i]:
            for j in range(2 * i, n + 1, i):
                ans[j] = False
    # ans is the bool array; ans[i] is True if i is prime, false otherwise
    if choice:
        return ans
    res = []
    for i in range(2, n + 1):
        if ans[i]:
            res.append(i)
    # res is the list of primes
    return res


sieve = sieve(10 ** 6, True)
sieve[1]=False
# print(sieve[1])
for _ in range(rn()):
    n, e = rns()
    a = rl()
    mods = defaultdict(list)
    for i in range(n):
        mods[i % e].append(a[i])
    ans = 0
    for group in mods.values():
        # print(group)
        for i in range(len(group)):
            if sieve[group[i]]:
                left=1
                j=i-1
                while j>=0 and group[j]==1:
                    j-=1
                    left+=1
                j=i+1
                right=1
                while j<len(group) and group[j]==1:
                    j+=1
                    right+=1
                ans+=left*right-1
    print(ans)
