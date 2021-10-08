from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7

k=rn()
ans=6
p=2**k-2
ans*=pow(4,p,mod)
print(ans%mod)
