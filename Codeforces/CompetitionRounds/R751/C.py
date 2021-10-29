from sys import stdin
from math import gcd
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
def factors(n):
    ans=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            ans.add(i)
            ans.add(n//i)
    return sorted(list(ans))
for _ in range(rn()):
    n=rn()
    a=rl()
    bits = [0]*31
    for num in a:
        b=bin(num)[2:]
        for i in range(len(b)):
            bits[-i-1] += int(b[-i-1])
    bits = [i for i in bits if i!=0]
    if len(bits)==0:
        print(*list(range(1,n+1)))
    else:
        g=bits[0]
        for i in range(1,len(bits)):
            g=gcd(g,bits[i])
        print(*factors(g))