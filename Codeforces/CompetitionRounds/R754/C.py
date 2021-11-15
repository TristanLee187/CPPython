from sys import stdin
from itertools import accumulate
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    def solve():
        if 'aa' in s:
            return 2
        for i in range(n-2):
            if s[i]==s[i+2]=='a':
                return 3
        for i in range(n-3):
            if s[i]==s[i+3]=='a' and {s[i+1],s[i+2]} == {'b','c'}:
                return 4
        for i in range(n-6):
            if s[i]==s[i+3]==s[i+6]=='a' and sorted([s[i+j] for j in [1,2,4,5]]) == ['b','b','c','c']:
                return 7
        return -1
    print(solve())