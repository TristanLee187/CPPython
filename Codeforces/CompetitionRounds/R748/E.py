from sys import stdin
from collections import defaultdict, Counter
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    n,k=rns()
    if n==1:
        print(0)
    else:
        tree=defaultdict(set)
        for __ in range(n-1):
            u,v=rns()
            tree[u].add(v)
            tree[v].add(u)
        # print(tree)
        ans=defaultdict(int)
        nodes=n
        depth=1
        leaves = [node for node in tree if len(tree[node]) <= 1]
        while nodes>0:
            # print(depth, ans)
            new_leaves = []
            for leaf in leaves:
                ans[leaf]=depth
                if tree[leaf]:
                    adj = tree[leaf].pop()
                    tree[adj].remove(leaf)
                    if len(tree[adj])==1:
                        new_leaves.append(adj)
                tree.pop(leaf)
            depth+=1
            nodes-=len(leaves)
            leaves = new_leaves
        # print(ans)
        # print(amts)
        pans=n
        # print(ans.values())
        for num in ans.values():
            if num<=k:
                pans-=1
        print(pans)
