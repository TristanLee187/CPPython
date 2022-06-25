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

def reduce(num, divisor):
    ans=1
    while num%divisor==0:
        num //= divisor
        ans*=divisor
    return [num, ans]

for _ in range(rn()):
    n,m=rns()
    a=rl()
    k=rn()
    b=rl()
    newa = []
    for i in range(n):
        if a[i]%m==0:
            newa.append(reduce(a[i], m))
        else:
            newa.append([a[i], 1])
    newb=[]
    for i in range(k):
        if b[i]%m==0:
            newb.append(reduce(b[i], m))
        else:
            newb.append([b[i], 1])
    conda=[newa[0]]
    for i in range(1, len(newa)):
        if newa[i][0] == conda[-1][0]:
            conda[-1][1] += newa[i][1]
        else:
            conda.append(newa[i])
    condb=[newb[0]]
    for i in range(1, len(newb)):
        if newb[i][0] == condb[-1][0]:
            condb[-1][1] += newb[i][1]
        else:
            condb.append(newb[i])
    # print(conda)
    # print(condb)
    YN(conda==condb)