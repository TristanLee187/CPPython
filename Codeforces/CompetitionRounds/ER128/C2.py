from sys import stdin
from collections import deque
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    def solve():
        s=rs()
        d=deque(s)
        while d and d[0]=='0':
            d.popleft()
        while d and d[-1]=='0':
            d.pop()
        if len(d)==0:
            return 0
        a=0
        b=d.count('0')
        ans=max(a,b)
        last=d[0]
        accs=[0]
        ids=[d[0]]
        for i in range(len(d)):
            if d[i]==last:
                accs[-1]+=1
            else:
                accs.append(1)
                ids.append(d[i])
                last=d[i]
        # print(accs)
        # print(ids)
        zero_groups=ids.count('0')
        zero_indeces=deque([i for i in range(len(ids)) if ids[i]=='0'])

        for i in range(zero_groups):
            test1 = max(a+accs[zero_indeces[0]-1], b-accs[zero_indeces[0]])
            test2 = max(a+accs[zero_indeces[-1]+1], b-accs[zero_indeces[-1]])
            if test1<test2:
                a+=accs[zero_indeces[0]-1]
                b-=accs[zero_indeces[0]]
                zero_indeces.popleft()
                ans=min(ans, max(a,b))
            else:
                a+=accs[zero_indeces[-1]+1]
                b-=accs[zero_indeces[-1]]
                zero_indeces.pop()
                ans=min(ans, max(a,b))

            print(ans, a, b)
        return ans
    print(solve())