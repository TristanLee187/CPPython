from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    p=[rl() for i in range(3)]
    ans=0
    for i in range(3):
        for j in range(i+1,3):
            if p[i][1]==p[j][1] and p[3-i-j][1]<p[i][1]:
                ans=p[i][0]-p[j][0]
    print(abs(ans))