from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

n,k=rns()
ans=0
for i in range(1,n+1):
    for j in range(1,k+1):
        ans+=100*i+j
print(ans)