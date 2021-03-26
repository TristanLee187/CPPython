rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    s=list(rs())
    ans=1
    i=0
    while i<n and s[i]!='*':
        i+=1
    s[i]='x'
    j=i+k
    while j<n and s[j]!='x':
        if s[j]=='*':
            s[j]='x'
            ans+=1
            j+=k
        else:
            j-=1
    for k in range(n-1,-1,-1):
        if s[k]=='x':
            break
        if s[k]=='*':
            ans+=1
            break
    print(ans)