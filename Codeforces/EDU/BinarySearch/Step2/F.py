t=input()
n=len(t)
p=input()
l=list(map(int,input().split()))
lo=0
hi=len(t)
ans=0
while lo<=hi:
    mid=(lo+hi+1)//2
    s=set(l[:mid])
    test=''
    for i in range(1,n+1):
        if i not in s:
            test+=t[i-1]
    j=0
    for i in range(len(test)):
        if j==len(p):
            break
        elif test[i]==p[j]:
            j+=1
    if j==len(p):
        ans=mid
        lo=mid+1
    else:
        hi=mid-1
print(ans)