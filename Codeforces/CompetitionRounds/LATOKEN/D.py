from sys import stdin, stdout
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

n=rn()
seen=set(range(1,n+1))
tree=defaultdict(set)
def solve(root,seen,tree,a):
    if root not in seen:
        return
    print(root,seen,tree)
    seen.remove(root)
    ones=set()
    twos=set()
    for i in range(n):
        num=a[i]
        if num==1:
            if i+1 in seen:
                ones.add(i+1)
            tree[root].add(i+1)
            tree[i+1].add(root)
        elif num==2 and i+1 in seen:
            twos.add(i+1)
    if len(ones)==0:
        if root in seen:
            seen.remove(root)
        return
    if len(ones)<len(twos):
        for nroot in ones:
            if nroot in seen:
                print('?',nroot)
                stdout.flush()
                b=rl()
                for i in range(n):
                    if b[i]==1:
                        tree[nroot].add(i + 1)
                        tree[i + 1].add(nroot)
                for i in range(n):
                    if b[i]==1 and i+1 in twos and i+1 in seen:
                        solve(i+1,seen,tree,b)
    else:
        for nroot in twos:
            if nroot in seen:
                print('?',nroot)
                stdout.flush()
                b=rl()
                for i in range(n):
                    if b[i] == 1:
                        tree[i+1].add(nroot)
                        tree[nroot].add(i + 1)
                for i in range(n):
                    if b[i]==1 and i+1 in ones and i+1 in seen:
                        solve(i+1,seen,tree,b)
print('? 1')
stdout.flush()
a=rl()
solve(1,seen,tree,a)
# print(tree)
seen.clear()
print('!')
def dfs(root,tree,seen):
    seen.add(root)
    for child in tree[root]:
        if child not in seen:
            seen.add(child)
            print(root,child)
            dfs(child,tree,seen)
dfs(1,tree,seen)
