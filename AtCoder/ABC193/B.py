rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
p=[]
for i in range(n):
    p.append(rl())
ans=float('inf')
for item in p:
    if item[2]-item[0]>0:
        ans=min(ans,item[1])
print(-1 if ans==float('inf') else ans)