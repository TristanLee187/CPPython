from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))
from math import ceil

t,n=rns()
a=100/t
ans=ceil(n*a)
ans=ans*(100+t)/100 - 1
print(int(ans))