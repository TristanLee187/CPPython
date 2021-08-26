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
    caves=[]
    for i in range(n):
        a=rl()[1:]
        a=[a[i]-i for i in range(len(a))]
        caves.append([max(a),len(a)])
    caves.sort()
    ans=0
    acc=0
    for i in range(n):
        ans=max(ans,caves[i][0]-acc+1)
        acc+=caves[i][1]
    print(ans)

