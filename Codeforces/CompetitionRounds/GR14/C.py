from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
import heapq

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


for _ in range(rn()):
    n,m,x=rns()
    a=rl()
    u=UnionFind(n)
    h=[]
    flag=True
    for i in range(n):
        heapq.heappush(h,[a[i],i])
    for i in range(n-m):
        d = heapq.heappop(h)
        e = heapq.heappop(h)
        if len(h)>0:
            f = heapq.heappop(h)
            if d[0]+e[0]-f[0] > x:
                flag=False
                break
            heapq.heappush(h, f)
        u.union(d[1],e[1])
        new = [d[0]+e[0],min(d[1],e[1])]
        heapq.heappush(h,new)
    ans=n*[0]
    for i in range(len(u.roots())):
        for j in u.members(u.roots()[i]):
            ans[j]=i+1
    YN(flag)
    if flag:
        print(*ans)
        print(u)