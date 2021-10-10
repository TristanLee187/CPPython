from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,c=rs().split()
    n=int(n)
    s=rs()
    a=set([i+1 for i in range(n) if s[i]!=c])
    # print(a)
    if len(a)==0:
        print(0)
    elif s[n-1]==c:
        print(1)
        print(n)
    else:
        found=False
        for i in range(n,n//2,-1):
            if i not in a:
                found=True
                print(1)
                print(i)
                break
        if not found:
            print(2)
            print(n-1,n)
