from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7

for _ in range(rn()):
    n, k = rns()
    def solve():
        if k == 0:
            return 1
        g = not n % 2
        s = 2*(n%2)
        add=1
        for i in range(n-2,0,-2):
            add*=(i*(i-1))
            add //= ((n-i+1)*(n-i+2))
            add%=mod
            s+=add
            s%=mod
            print(f's {s}')
        ans=pow(s,k,mod)
        if g:
            for i in range(k):
                ans+=pow(s,n-i-1,mod)*pow(pow(2,n,mod),i,mod)
                ans%=mod
        return ans
    print(solve())