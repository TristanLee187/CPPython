from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from itertools import accumulate

n=rn()
a=rl()
b=rl()
prods = [a[i]*b[i] for i in range(n)]
pre = list(accumulate(prods))
suff = list(accumulate(prods[::-1]))[::-1]
ans = pre[-1]
# swaps=[]
# for i in range(n):
#     swaps.append([])
#     for j in range(i+1,n):
#         swaps[-1].append((a[i]-a[j])*(b[j]-b[i]))

# print(swaps)
change = 0
for i in range(2*(n-1)-1):
    if i==0 or i==1:
        change = max(change, (a[i+1]-a[0])*(b[0]-b[i+1]))
    else:
        acc=0
        x=i%2
        y=i//2
        while y>=0 and x<n-1-y:
            acc+=(a[y]-a[y+x+1])*(b[y+x+1]-b[y])
            change = max(change, acc)
            y-=1
            x+=2

print(ans+change)