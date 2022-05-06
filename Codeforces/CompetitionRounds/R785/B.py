from sys import stdin
from math import ceil
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    s=rs()
    n=len(s)
    def solve():
        if len(set(s))==1:
            return True
        else:
            pre=s[0]
            seen=set(s[0])
            for i in range(n-1):
                if i==0:
                    if s[1]==s[0]:
                        break
                    else:
                        pre+=s[1]
                        seen.add(s[1])
                else:
                    if s[i+1]==s[0]:
                        break
                    elif s[i+1] not in seen:
                        pre+=s[i+1]
                        seen.add(s[i+1])
                    else:
                        return False
            # print(pre)
            return s in ceil(n/len(pre))*pre
    YN(solve())