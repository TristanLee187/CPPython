from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    if n==2:
        print(-1)
    else:
        ans=[]
        for i in range(n):
            ans.append(n*[0])
        num=1
        for i in range(n-1,-1,-2):
            for j in range(n-i):
                ans[j][i+j]=num
                num+=1
        start=1 if n%2==0 else 2
        for i in range(start,n,2):
            for j in range(n - i):
                ans[i+j][j] = num
                num += 1
        for i in range(n-2,-1,-2):
            for j in range(n - i):
                ans[j][i+j] = num
                num += 1
        start=2-n%2
        for i in range(start,n,2):
            for j in range(n - i):
                ans[i + j][j] = num
                num += 1
        for row in ans:
            print(*row)