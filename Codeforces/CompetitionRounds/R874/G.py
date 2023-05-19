import sys
from io import BytesIO, IOBase
import os
from collections import defaultdict
sys.setrecursionlimit(2*10**5)

# region fastio
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion

rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    adj=defaultdict(list)
    edges=[]
    for i in range(n-1):
        u,v=rns()
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u,v))
    tree=defaultdict(list)
    seen=set()
    stack=[1]
    while stack:
        p=stack.pop()
        seen.add(p)
        c=[i for i in adj[p] if i not in seen]
        tree[p]=c
        stack+=c
    bfs_levels=[[1]]
    while True:
        nl=[]
        for i in bfs_levels[-1]:
            nl+=tree[i]
        if nl:
            bfs_levels.append(nl)
        else:
            break
    cut=set()
    ccount=defaultdict(int)
    for level in bfs_levels[::-1]:
        for i in level:
            if tree[i]:
                ccount[i]=sum([ccount[j] for j in tree[i]])+1
            else:
                ccount[i]=1

    def dfs(root):
        if ccount[root]<3:
            return False
        if ccount[root]==3:
            return True
        for child in tree[root]:
            if ccount[child]%3==0:
                cut.add((root, child))
                ccount[root]-=ccount[child]
                if not dfs(child):
                    return False
            elif ccount[child]>3:
                if not dfs(child):
                    return False
        return not(sum([ccount[child] for child in tree[root]])>=3 and all([ccount[child]<3 for child in tree[root]]))

    if dfs(1):
        print(len(cut))
        pans=[]
        for i in range(n-1):
            u,v = edges[i]
            if (u,v) in cut or (v,u) in cut:
                pans.append(i+1)
        print(*pans)
    else:
        print(-1)

