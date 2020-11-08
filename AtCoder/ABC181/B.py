rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

n=rn()
ans=0
for i in range(n):
    a,b=rns()
    if (b-a)%2==1:
        ans+=(a+b)*(b-a+1)/2
    else:
        ans += (a + b) * (b - a) / 2 + (a+b)//2
print(int(ans))