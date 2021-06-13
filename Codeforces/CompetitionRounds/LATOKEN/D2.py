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
    seen.remove(root)
    ones=set()
    twos=set()
    for i in range(n):
        num=a[i]
        if num==1 and i+1 in seen:
            ones.add(i+1)
            tree[root].add(i+1)
        elif num==2 and i+1 in seen:
            twos.add(i+1)
    if len(ones)==0:
        return
    if len(ones)<len(twos):
        for nroot in ones:
            print('?',nroot)
            stdout.flush()
            b=rl()
            for i in range(n):
                if i+1 in twos and b[i]==1:
                    tree[nroot].add(i+1)
                    solve(nroot,seen,tree,b)
    else:
        for nroot in twos:
            print('?',nroot)
            stdout.flush()
            b=rl()
            for i in range(n):
                if i+1 in ones and b[i]==1:
                    tree[i+1].add(nroot)
                    solve(nroot,seen,tree,b)
print('? 1')
stdout.flush()
a=rl()
solve(1,seen,tree,a)
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