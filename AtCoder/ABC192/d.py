rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

x=rs()
m=rn()
if len(x)==1:
    if m>=int(x):
        print(1)
    else:
        print(0)
else:
    lo=1
    hi=10**18+1
    ans=0
    while lo<=hi:
        mid=(lo+hi+1)//2
        acc=0
        for i in range(len(x)):
            acc+=int(x[::-1][i])*mid**i
        if acc<=m:
            ans=mid
            lo=mid+1
        else:
            hi=mid-1
    dig=int(max(list(x)))
    print(max(ans-dig,0))