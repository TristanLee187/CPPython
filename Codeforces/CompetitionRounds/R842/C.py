import sys
from io import BytesIO, IOBase
import os
from collections import Counter, defaultdict

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
    a=rl()
    sa=sorted(a)
    check = [i+1>sa[i] for i in range(n)]
    c=Counter(a)
    check2 = [i>2 for i in c.values()]
    if any(check + check2):
        print('NO')
    else:
        print('YES')
        p=n*[0]
        q=n*[0]
        pseen=set()
        qseen=set()
        for i in range(n):
            if i==0 or sa[i]!=sa[i-1]:
                p[i]=sa[i]
                pseen.add(sa[i])
            else:
                q[i]=sa[i]
                qseen.add(sa[i])
        # print(pseen)
        # print(qseen)
        pnums=[i for i in range(n,0,-1) if i not in pseen]
        qnums=[i for i in range(n,0,-1) if i not in qseen]
        # print(pnums)
        # print(qnums)
        for i in range(n):
            if p[i]==0:
                p[i]=pnums.pop()
            if q[i]==0:
                q[i]=qnums.pop()
        # print(p)
        # print(q)
        pd=defaultdict(list)
        qd=defaultdict(list)
        for i in range(n):
            pd[sa[i]].append(p[i])
            qd[sa[i]].append(q[i])
        pans=[]
        qans=[]
        for num in a:
            pans.append(pd[num].pop())
            qans.append(qd[num].pop())
        print(*pans)
        print(*qans)
