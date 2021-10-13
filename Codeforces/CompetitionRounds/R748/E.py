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
            ans[leaf]=max(ans[leaf],depth)
            if tree[leaf]:
                adj = list(tree[leaf])[0]
                tree[adj].remove(leaf)
                if len(tree[adj])==1:
                    new_leaves.append(adj)
            tree.__delitem__(leaf)
        depth+=1
        nodes-=len(leaves)
        leaves = new_leaves.copy()
    # print(ans)
    amts = Counter(ans.values())
    # print(amts)
    pans=n
    for i in range(k):
        pans-=amts[i+1]
    print(pans)