rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,m=rns()
l=rl()
o=[]
for i in range(m):
    o.append(rl())
a=[]
for i in range(n):
    a.append([l[i],i])
a.sort()
start=1
ans=[]
for i in range(1,n):
    if a[i][1]<a[i-1][1]:
        start+=1
ans.append(start)
for i in range(m):
    [b,c]=sorted(o[i])
    b-=1
    c-=1
    lb=l[b]-1
    lc=l[c]-1
    [lb,lc]=sorted([lb,lc])
    og = 1
    if lc==lb+1:
        s1=a[max(0,lb-1):min(n,lb+2)]
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                og+=1
        s1=a[lc:min(n,lc+2)]
        og+=1
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                og+=1
    else:
        s1=a[max(0,lb-1):min(n,lb+2)]
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                og+=1
        s1=a[max(0,lc-1):min(n,lc+2)]
        og+=1
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                og+=1
    a[l[c]-1][1],a[l[b]-1][1]=a[l[b]-1][1],a[l[c]-1][1]
    l[c],l[b]=l[b],l[c]
    [b, c] = sorted(o[i])
    b -= 1
    c -= 1
    lb = l[b] - 1
    lc = l[c] - 1
    [lb, lc] = sorted([lb, lc])
    diff=1
    if lc==lb+1:
        s1=a[max(0,lb-1):min(n,lb+2)]
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                diff+=1
        s1=a[max(0,lc):min(n,lc+2)]
        diff+=1
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                diff+=1
    else:
        s1=a[max(0,lb-1):min(n,lb+2)]
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                diff+=1
        s1=a[max(0,lc-1):min(n,lc+2)]
        diff+=1
        for i in range(1,len(s1)):
            if s1[i][1]<s1[i-1][1]:
                diff+=1
    ans.append(ans[-1]-og+diff)
    print(ans[-1],og,diff)

##DO NOT TRY THIS AT HOME