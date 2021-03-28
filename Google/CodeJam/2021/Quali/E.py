rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
from math import log, e

def g(x):
    return (log(e**(x+3)+1,e)-log(e**(x-3)+1,e))/6

t=rn()
p=rn()
for _ in range(t):
    a=[]
    for i in range(100):
        a.append(rs().count('1'))

    a.sort()
    for i in range(100):
        skill = -3 + 6*i/100
        exp = g(skill)
        a[i] = abs(exp - a[i]/10000)

    ans=a.index(max(a))+1
    print('Case #' + str(_+1)+': ' + str(ans))