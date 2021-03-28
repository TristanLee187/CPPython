rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    s=rs()
    ans=''
    count=0
    for i in s:
        if i=='b':
            count+=1
        else:
            ans+=i
    ans=count*'b'+ans
    print(ans)