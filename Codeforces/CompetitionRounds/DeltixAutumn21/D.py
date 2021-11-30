from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
ceil_div = lambda a, b: -(-a // b)
mod = 10 ** 9 + 7


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x) -> int:
        return -self.parents[self.find(x)]

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x) -> list:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list:
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self) -> dict:
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, d = rns()
extra=0
U=UnionFind(n)
for _ in range(d):
    a,b=rns()
    a-=1
    b-=1
    if U.same(a,b):
        extra+=1
    else:
        U.union(a,b)
    d=[U.size(i) for i in U.roots()]
    d.sort(reverse=True)
    ans=sum(d[:extra+1])
    print(ans-1)