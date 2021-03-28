import math
from decimal import *

def equals(x,y):
    return max(x,y)-min(x,y) < 10**(-18)

t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    a=l[0]
    b=l[1]

    d = max(a,b)
    c = min(a,b)

    tcount=0
    broken = False
    while c<d:
        c *= 2
        tcount+=1
        if c>d:
            broken = True
            break
        elif c==d:
            break
    if broken:
        print(-1)
    else:
        print(math.ceil(tcount/3))
