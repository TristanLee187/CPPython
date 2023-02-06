import sys
from io import BytesIO, IOBase
import os

rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    c=rn()
    prevc=c
    ans=0
    curr=0
    for i in range(c):
        print("- {}".format(2**curr, curr))
        sys.stdout.flush()
        nextc=rn()
        if nextc==-1:
            quit()
        ans+=2**(curr+nextc-prevc+1)
        curr+=nextc-prevc+2
        prevc=nextc
    print('! {}'.format(ans))
