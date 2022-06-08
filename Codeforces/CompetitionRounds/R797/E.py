import sys
from io import BytesIO, IOBase
import os
from collections import defaultdict

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
    n,k=rns()
    a=rl()
    mods = defaultdict(list)
    for i in range(n):
        mods[a[i]%k].append(i)
    pairs=[]
    seen=set()
    for mod in mods:
        if (k-mod)%k in mods:
            m=min(len(mods[mod]), len(mods[(k-mod)%k]))
            if mod == (k-mod)%k:
                for i in range(m//2):
                    pairs.append([mods[mod][i], mods[mod][m-i-1]])
                    seen.add(pairs[-1][0])
                    seen.add(pairs[-1][1])
                if m%2==1:
                    mods[mod] = [mods[mod][m//2]]
                else:
                    mods[mod].clear()
            else:
                for i in range(m):
                    pairs.append([mods[mod].pop(), mods[(k-mod)%k].pop()])
                    seen.add(pairs[-1][0])
                    seen.add(pairs[-1][1])
    new = []
    for mod in mods:
        for i in range(len(mods[mod])):
            new.append([mod, mods[mod][i]])
    new.sort()
    i=0
    j=len(new)-1
    while i<j:
        summ = new[i][0] + new[j][0]
        if summ > k:
            pairs.append([new[i][1], new[j][1]])
            seen.add(new[i][1])
            seen.add(new[j][1])
            j-=1
        i+=1
    notused = [i for i in range(n) if i not in seen]
    for i in range(0,len(notused),2):
        pairs.append([notused[i], notused[i+1]])
    ans=0
    for pair in pairs:
        ans += (a[pair[0]] + a[pair[1]])//k
    print(ans)
