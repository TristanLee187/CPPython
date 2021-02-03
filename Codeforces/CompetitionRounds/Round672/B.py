rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=0
    for i in range(1,n):
        for j in range(i):
            if l[i]&l[j]>=l[i]^l[j]:
                ans+=1
    print(ans)