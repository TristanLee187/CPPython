from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

s=rs()
d={'0':'0','1':'1','6':'9','8':'8','9':'6'}
s=s[:-1][::-1]
s=''.join([d[i] for i in s])
print(s)