from math import *

for _ in range(int(input())):
    a,b,q=map(int,input().split())
    lcm = (a*b)//gcd(a,b)
    for i in range(q):
        l,r=map(int,input().split())
        left=l//lcm*lcm
        right=ceil(r/lcm)*lcm
        ans=0
        if (right-left)//lcm==1:
            if left+max(a,b)>l:
                ans+=max(0,r-l-(left+max(a,b)-l)+(r!=right))
            else:
                ans+=r-l+(r!=right)
        else:
            ans+=(left+lcm-l)
            if left+max(a,b)>l:
                ans-=left+max(a,b)-l
            ans+=r-(right-lcm)
            if r!=right:
                ans+=1
            if r>right-lcm+max(a,b):
                ans-=min(max(a,b),r-right+lcm-max(a,b))
            ans+=((right-left)//lcm-2)*(lcm-max(a,b))

        if i==q-1:
            print(ans)
        else:
            print(ans, end=' ')