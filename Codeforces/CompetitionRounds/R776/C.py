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
    rs()
    n,m=rns()
    p=[rl()+[i] for i in range(m)]
    p.sort(key=lambda x:[x[1],x[0]])
    w = [pair[1] for pair in p]
    s=sum(w[:2*n])
    print(s)
    indeces=[[p[i][0],p[i][2]] for i in range(2*n)]
    indeces.sort()
    for i in range(n):
        print(indeces[i][1]+1, indeces[2*n-i-1][1]+1)
    print()
