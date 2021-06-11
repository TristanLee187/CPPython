from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from bisect import bisect_left, bisect_right

for _ in range(rn()):
    n,l,r=rns()
    a=rl()
    a.sort()
    ans=0
    for num in a:
        left=bisect_left(a,l-num)
        right=bisect_right(a,r-num)
        if (left<n and num>=a[left]) and (0<right<=n and num<=a[right-1]):
            ans-=1
        ans+=right-left
        # print(right,left,ans)
    print(ans//2)