from sys import stdin
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m=rns()
    coms=defaultdict(defaultdict)
    heads=set()
    start=-1
    for __ in range(m):
        i,j,s=rs().split()
        i=int(i)
        start=i
        j=int(j)
        s=s[0]
        coms[i][j]=s
        heads.add(i)
    # print(coms)
    assigns = {
        'i':{'i':'c', 'c':'i'},
        'c':{'i':'i', 'c':'c'}
    }
    def solve(node, nodes, assign, coms,seen):
        nodes[node]=assign
        seen[node]=1
        # print(node, nodes)
        for adj in coms[node]:
            said=assigns[assign][coms[node][adj]]
            # print(node, adj, said)
            if adj in nodes:
                if nodes[adj]!=said:
                    # print('YIKE')
                    return -1
            else:
                nodes[adj]=said
                ans = solve(adj,nodes,said,coms,seen)
                if ans==-1:
                    return -1
    def calc(nodes,n):
        ans=n
        for node in nodes:
            if nodes[node]=='c':
                ans-=1
        return ans
    seen={}
    ans=0
    for node in heads:
        if node not in seen:
            nodes = defaultdict(int)
            a = solve(node, nodes, 'i', coms,seen)
            c1=calc(nodes,n)
            # print(nodes)

            nodes2 = defaultdict(int)
            b = solve(node, nodes2, 'c', coms,seen)
            c2=calc(nodes2,n)
            # print(nodes2)

            if a==b==-1:
                ans=-1
                break
            else:
                take=[]
                if c1>c2:
                    take=nodes
                else:
                    take=nodes2
                for node in take:
                    seen[node]=take[node]
    if ans==-1:
        print(-1)
    else:
        ans=calc(seen,n)
        print(ans)

