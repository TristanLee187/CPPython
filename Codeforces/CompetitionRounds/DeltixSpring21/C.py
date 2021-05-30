from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

for _ in range(rn()):
    n=rn()
    a=[rn() for _ in range(n)]
    used=defaultdict(set)
    ans=[[1]]
    for i in range(1,n):
        if a[i]==1:
            ans.append(ans[-1]+[1])
        else:
            mlen = float('inf')
            for j in range(len(ans)-1,-1,-1):
                if ans[j][-1] == a[i]-1 and tuple(ans[j][:-1]) not in used[a[i]] and len(ans[j])<mlen:
                    ans.append(ans[j][:-1]+[a[i]])
                    used[a[i]].add(tuple(ans[j][:-1]))
                    break
                else:
                    mlen=min(mlen,len(ans[j]))
    for line in ans:
        print('.'.join(list(map(str,line))))

