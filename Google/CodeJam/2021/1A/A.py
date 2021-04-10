rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    n=rn()
    a=rl()
    ans=0
    for i in range(1,n):
        diff = a[i]-a[i-1]-1
        if diff<0:
            diff*=-1
            test=10
            add=1
            while diff-(test-1)*a[i]>test-1:
                add+=1
                test*=10
            ans+=add
            a[i] += (test-1)*a[i] + max(diff-(test-1)*a[i],0)

    print('Case #' + str(_+1)+': ' + str(ans))