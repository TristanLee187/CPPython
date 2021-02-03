"""
ID: tristan16
LANG: PYTHON3
PROB: milk
"""

a=open('milk.in','r')
b=open('milk.out','w')

n,m=map(int,a.readline().split())

ans=[]
for i in range(m):
    l=list(map(int,a.readline().split()))
    ans.append(l)
ans=sorted(ans)

c=0
for i in range(m):
    c+=min(n,ans[i][1])*ans[i][0]
    n-=min(n,ans[i][1])
    if n==0:
        break

b.write(str(c)+'\n')
a.close()
b.close()
