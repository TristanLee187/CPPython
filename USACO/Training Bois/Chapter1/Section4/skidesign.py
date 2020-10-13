"""
ID: tristan16
LANG: PYTHON3
PROB: skidesign
"""

import math

a=open('skidesign.in', 'r')
b=open('skidesign.out', 'w')

cast=int
r=range

n=cast(a.readline())
l=[]
for i in r(n):
    l.append(cast(a.readline()))
l=sorted(l)


p1=0
p2=0
spaces=[]
while p2<n and l[p2]-l[p1]<=17:
    p2+=1
    spaces.append(0)
for i in range(p2,n):
    spaces.append(l[i]-l[p1]-17)

ans=0
print(spaces)



b.write(str(ans)+'\n')

a.close()
b.close()