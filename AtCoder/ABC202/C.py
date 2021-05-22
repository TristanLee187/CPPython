from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))
from collections import Counter, defaultdict

n=rn()
a=rl()
b=rl()
c=rl()
A=Counter(a)
C=Counter(c)
B=defaultdict(list)
for i in range(n):
    B[b[i]].append(i+1)
ans=0
for num in A:
    base=A[num]
    for j in B[num]:
        ans+=base*C[j]
print(ans)
