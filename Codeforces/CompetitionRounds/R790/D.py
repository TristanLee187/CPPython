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
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n,m=rns()
    grid=[rl() for i in range(n)]
    sgrid=[[0 for i in range(m)] for j in range(n)]
    def sumdiag_up(i,j,vals,board):
        ans=0
        r,c=i,j
        while 0<=r<n and 0<=c<m:
            ans+=vals[r][c]
            r-=1
            c+=1
        r,c=i,j
        while 0<=r<n and 0<=c<m:
            board[r][c]+=ans
            r-=1
            c+=1
    def sumdiag_down(i,j,vals,board):
        ans=0
        r,c=i,j
        while 0<=r<n and 0<=c<m:
            ans+=vals[r][c]
            r+=1
            c+=1
        r,c=i,j
        while 0<=r<n and 0<=c<m:
            board[r][c]+=ans
            r+=1
            c+=1
    for i in range(n):
        sumdiag_up(i,0,grid,sgrid)
    for j in range(1, m):
        sumdiag_up(n-1,j,grid,sgrid)
    for i in range(n-1,-1,-1):
        sumdiag_down(i,0,grid,sgrid)
    for j in range(1,m):
        sumdiag_down(0,j,grid,sgrid)
    vals=[]
    for i in range(n):
        for j in range(m):
            vals.append(sgrid[i][j] - grid[i][j])
    print(max(vals))
