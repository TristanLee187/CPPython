"""
ID: tristan16
LANG: PYTHON3
PROB: milk2
"""

import bisect

a=open('milk2.in','r')
b=open('milk2.out','w')
n=int(a.readline())

starts=[]
ends=[]
for i in range(n):
    m,k=map(int,a.readline().split())
    j=bisect.bisect_left(starts,m)
    starts.insert(j,m)
    ends.insert(j,k)
left=starts[0]
right=ends[0]
ans1=right-left
ans2=0

for i in range(1,n):
    if starts[i]<=right and starts[i]>=left and ends[i]>=right:
        right=ends[i]
    elif starts[i]>right and ends[i]>right:
        ans2=max(ans2,starts[i]-right)
        ans1=max(ans1,right-left)
        left=starts[i]
        right=ends[i]

b.write(str(ans1)+' '+str(ans2)+'\n')
a.close()
b.close()

    
