import sys
from io import BytesIO, IOBase
import os

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
YN=lambda x:sys.stdout.write(('YES' if x else 'NO') + '\n')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n,m=rns()
    grid=[rl() for i in range(n)]
    max_grid = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                max_grid[0][0]=grid[0][0]
            elif i==0:
                max_grid[0][j] = max_grid[0][j-1]+grid[i][j]
            elif j==0:
                max_grid[i][0] = max_grid[i-1][0]+grid[i][j]
            else:
                max_grid[i][j] = max(max_grid[i - 1][j], max_grid[i][j-1]) + grid[i][j]

    min_grid = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i==j==0:
                min_grid[0][0]=grid[0][0]
            elif i==0:
                min_grid[0][j] = min_grid[0][j-1]+grid[i][j]
            elif j==0:
                min_grid[i][0] = min_grid[i-1][0]+grid[i][j]
            else:
                min_grid[i][j] = min(min_grid[i - 1][j], min_grid[i][j-1]) + grid[i][j]

    def solve():
        if (n+m-1)%2==1:
            return False
        # print(min_grid[-1][-1], max_grid[-1][-1])
        return min_grid[n-1][m-1]<=0<=max_grid[n-1][m-1]

    YN(solve())
