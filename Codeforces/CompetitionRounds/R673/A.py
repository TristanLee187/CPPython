rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    n,k=rns()
    l=rl()
    l.sort()
    ans=0
    for i in range(1,n):
        a=k-l[i]
        ans+=a//l[0]
    print(ans)
