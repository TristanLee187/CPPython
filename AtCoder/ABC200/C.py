from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))
from collections import Counter

n=rn()
a=rl()
a=[i%200 for i in a]
ans=0
c=Counter(a)
for i in a:
    c[i]-=1
    ans+=c[i]
print(ans)