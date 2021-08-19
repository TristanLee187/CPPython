from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

a=[]
b=1
while b<10**18:
    a.append(b)
    b*=2
def f(a,b):
    ans=0
    p=0
    i=0
    while i<len(a) and p<len(b):
        if a[i]==b[p]:
            p+=1
        else:
            ans+=1
        i+=1
    ans+=len(b)-p+len(a)-i
    return ans

for _ in range(rn()):
    n=rn()
    ans=float('inf')
    for num in a:
        ans=min(ans, f(str(n),str(num)))
    print(ans)