rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

for _ in range(rn()):
    n=rn()
    c=rl()
    a=rl()
    b=rl()
    ans=0
    curr=c[-1]
    for i in range(n-1,-1,-1):
        if i==0:
            ans=max(ans,curr)
        elif a[i]==b[i]:
            curr+=1
            ans=max(ans,curr)
            curr=c[i-1]
        else:
            curr = max(curr, c[i])
            if i==1:
                curr+=abs(b[i]-a[i])+1
            else:
                ans = max(ans, curr + abs(b[i]-a[i])+1)
                curr+=min(a[i],b[i])+c[i-1]-max(a[i],b[i])+1
    print(ans)