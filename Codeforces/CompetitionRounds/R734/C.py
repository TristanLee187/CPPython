from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter

for _ in range(rn()):
    n=rn()
    words=[rs() for i in range(n)]
    ans=0
    d=[Counter(word) for word in words]
    for char in ['a','b','c','d','e']:
        poss=0

        diffs=[]
        for i in range(n):
            diff=len(words[i])-2*d[i][char]
            diffs.append(diff)
        diffs.sort()
        acc=0
        for i in range(n):
            if acc+diffs[i]>=0:
                break
            acc+=diffs[i]
            poss+=1
        ans=max(ans,poss)
    print(ans)
