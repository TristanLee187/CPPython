from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

a=rl()
a.sort()
if a[0]==a[1]:
    print(a[2])
elif a[1]==a[2]:
    print(a[0])
else:
    print(0)