rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n=rn()
    l=rl()
    s=l[0]
    ts=0
    ans=0
    c=1
    i=1
    while i<n:
        if l[i]==s:
            c+=1
        else:
            ts+=l[i]
            if ts>l[i]:
                ans+=1
            if ts>s:
                s=c*s+ts
                ts=0
                ans+=c
                c=1
            elif ts==s:
                ts=0
                c+=1
        i+=1
        print(ans,s,ts,c)
    if 0<ts<s:
        ans=n-1
    print(ans)