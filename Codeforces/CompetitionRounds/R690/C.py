rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    if n>45:
        print(-1)
    else:
        ans=''
        sum=0
        last=0
        for i in range(9,0,-1):
            sum+=i
            last=i
            if sum>n:
                sum-=i
                last=i+1
            else:
                ans=str(i)+ans
        if sum!=n:
            for i in range(1,last):
                if sum+i==n:
                    ans=str(i)+ans
                    sum+=i
        if sum==n:
            print(ans)