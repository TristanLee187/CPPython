rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n,k=rns()
    l=rl()
    #diff=[abs(l[i]-l[i-1]) for i in range(1,n)]
    #ans=max(diff)<=2*k-2
    left=l[0]
    right=k+l[0]
    ans=True
    for i in range(1,n-1):
        if not (l[i]>=l[i-1] and left<=l[i]<right) and not (l[i]<=l[i-1] and left<l[i]+2*k-1):
            ans=False
            break
        elif left<=l[i]<right:
            left=l[i]
            right=min(right+k-1,l[i]+2*k-1)
        else:
            left=max(l[i],left-k+1)
            right=l[i]+2*k-1
        print(left,right)
    if not (l[-1]>=l[-2] and left<=l[-1]<right) and not (l[-1]<=l[-2] and left<l[-1]+k):
        ans=False
    YN(ans)
