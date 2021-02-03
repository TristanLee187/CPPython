rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

import operator as op
from functools import reduce

def ncr(n, r):
    if n<r:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

for _ in range(rn()):
    n=rn()
    l=rl()
    l.sort()
    a=(n+1)*[0]
    for i in l:
        a[i]+=1
    ans=0
    add=0
    for i in range(n+1):
        if add==0:
            acc=a[i]
            if i<n:
                acc+=a[i+1]
            if i<n-1:
                acc+=a[i+2]
            ans+=ncr(acc,3)
            add=acc-a[i]
        else:
            acc = a[i]
            if i < n:
                acc += a[i + 1]
            if i < n - 1:
                acc += a[i + 2]
            ans += max(ncr(acc, 3) - ncr(add,3),0)
            add = acc - a[i]
    print(ans)