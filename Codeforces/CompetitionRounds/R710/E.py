rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7
from bisect import bisect_left

for _ in range(rn()):
    n = rn()
    a = rl()
    s=set(a)
    left=set(range(1,n+1))
    ans=[]
    for i in a:
        if i in s:
            ans.append(i)
            s.remove(i)
            left.remove(i)
        else:
            ans.append(0)
    left=list(left)

    # mins
    i=0
    mins=ans.copy()
    for j in range(n):
        if ans[j]==0:
            mins[j]=left[i]
            i+=1

    # maxes
    maxes=ans.copy()
