import sys
from math import ceil
l=1
r=1000000
while l<r-1:
    mid=(l+r)//2
    print(mid,l,r)
    sys.stdout.flush()
    s=input()
    if s=='<':
        r=mid-1
    else:
        l=mid
print(r)
if input()=='<':
    print('!',l)
else:
    print('!',r)
