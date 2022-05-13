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
        left=[]
        for i in range(0,len(accs)-1,2):
            left.append([accs[i], accs[i+1]])
        left.append([accs[-1],0])
        right=[]
        for i in range(len(accs)-1, 0, -2):
            right.append([accs[i], accs[i-1]])
        right.append([accs[0],0])
        right.reverse()
        # print(left)
        # print(right)
        left_p=0
        a+=left[left_p][0]
        b-=left[left_p][1]
        ans=min(ans, max(a,b))
        right_p=len(left)
        while right_p>left_p+1:
            testa, testb = a+right[right_p-1][0], b-right[right_p-1][1]
            if max(testa, testb) < max(a,b):
                a=testa
                b=testb
                ans=min(ans, max(a,b))
                right_p-=1
            else:
                break
        print(left)
        print(right)
        for i in range(1,len(left)):
            # print(a,b)
            left_p=i
            a += left[left_p][0]
            b -= left[left_p][1]
            if left_p==right_p:
                a -= right[right_p][0]
                b += right[right_p][1]
                right_p+=1
            ans = min(ans, max(a, b))
            while right_p<len(left):
                testa, testb = a - right[right_p][0], b + right[right_p][1]
                if max(testa,testb)<max(a,b):
                    a=testa
                    b=testb
                    right_p+=1
                    ans=min(ans,max(a,b))
                else:
                    break
            ans = min(ans, max(a, b))

        return ans
    print(solve())