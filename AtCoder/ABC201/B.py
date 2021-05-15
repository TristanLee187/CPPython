from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

n=rn()
m=[]
for i in range(n):
    tag=input().split()[::-1]
    tag[0]=int(tag[0])
    m.append(tag)
m.sort()
print(m[-2][1])