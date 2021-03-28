from math import *

t=int(input())
for _ in range(t):
    n=int(input())
    s=ceil(n/4)
    print((n-s)*'9'+s*'8')


