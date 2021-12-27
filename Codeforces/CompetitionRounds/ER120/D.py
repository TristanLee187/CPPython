from sys import stdin
from itertools import accumulate
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=998244353


def make_nCr_mod(max_n=5000):
    max_n = min(max_n, mod - 1)

    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod



n,k=rns()
a=list(map(int,rs()))
acc=list(accumulate(a))
# print(acc)
def solve():
    j=0
    ans=1
    choose=make_nCr_mod()
    first=True
    for i in range(n):
        # j+=1
        if j==n:
            break
        while j<n and acc[j]-acc[i]+a[i]<=k:
            if acc[j]-acc[i]+a[i]==k:
                add=0
                if not first:
                    if a[j]==0:
                        add=choose(j-i,k-1)
                    elif j-i+1>k:
                        add=choose(j-i,k)
                else:
                    if a[j]==0:
                        add=choose(j-i+1,k-1)-1
                    elif j-i+1>k:
                        add=choose(j-i+1,k)-1
                    first=False
                ans+=add
                ans%=mod
                # print(i,j,add)
            j+=1
    return ans
print(solve())
