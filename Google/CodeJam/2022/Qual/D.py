from sys import stdin
from collections import defaultdict
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    n=rn()
    f=rl()
    p=rl()
    tree=defaultdict(list)
    roots={i for i in range(1,n+1)}
    for i in range(n):
        if p[i]!=0:
            tree[p[i]].append(i+1)
            roots.remove(i+1)

    # print(tree)
    # print(roots)
    maxes=defaultdict(int)
    def sub_maxes(root):
        if root not in tree or len(tree[root])==0:
            maxes[root]=f[root-1]
            return f[root-1]
        nums = [sub_maxes(child) for child in tree[root]]
        maxes[root] = max(min(nums), f[root-1])
        return maxes[root]
    for root in roots:
        sub_maxes(root)

    def solve(root):
        if root not in tree or len(tree[root])==0:
            return maxes[root]
        else:
            nums = [solve(child) for child in tree[root]]
            ans = sum(nums)
            m = min([maxes[child] for child in tree[root]])
            if f[root-1]>m:
                ans+=f[root-1]-m
            return ans

    for root in roots:
        ans += solve(root)

    print('Case #' + str(_+1)+': ' + str(ans))