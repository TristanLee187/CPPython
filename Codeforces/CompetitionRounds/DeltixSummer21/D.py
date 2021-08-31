from sys import stdin
from sys import stdout
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,k=rns()
ands={}
ors={}
for i in range(1,n):
    print('and {} {}'.format(1,i+1))
    stdout.flush()
    ands[(1,i+1)]=rn()
    print('or {} {}'.format(1, i + 1))
    stdout.flush()
    ors[(1, i+1)] = rn()
print('and {} {}'.format(2,3))
stdout.flush()
ands[(2,3)]=rn()
print('or {} {}'.format(2,3))
stdout.flush()
ors[(2,3)]=rn()
a=(ands[(1,2)]+ors[(1,2)]+ands[(1,3)]+ors[(1,3)]-(ands[(2,3)]+ors[(2,3)]))//2
l=[a]
for i in range(1,n):
    num=ands[(1,i+1)]+ors[(1,i+1)]-a
    l.append(num)
l.sort()
ans=l[k-1]
print('finish {}'.format(ans))
stdout.flush()
