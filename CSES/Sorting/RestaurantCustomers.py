rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))

n=rn()
p=[]
for i in range(n):
    a,b=rl()
    p.append([a,1])
    p.append([b,-1])
p.sort()
ans=0
sum=0
for i in range(2*n):
    sum+=p[i][1]
    ans=max(ans,sum)
print(ans)