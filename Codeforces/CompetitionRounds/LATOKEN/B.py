from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    def solve(n,a):
        if n==1:
            return a[0]
        c=0
        for i in range(n):
            if i==0 and a[i]>a[i+1]:
                c+=a[i]-a[i+1]
                a[i]=a[i+1]
            elif i==n-1 and a[i]>a[i-1]:
                c+=a[i]-a[i-1]
                a[i]=a[i-1]
            elif 0<i<n-1 and a[i]>a[i+1] and a[i]>a[i-1]:
                c+=a[i]-max(a[i+1],a[i-1])
                a[i]=max(a[i+1],a[i-1])
        for i in range(n):
            if i==0:
                c+=a[i]
            else:
                c+=abs(a[i]-a[i-1])
        c+=a[-1]
        return c
    print(solve(n,a))