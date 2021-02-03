rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    s=rs()
    n=len(s)
    d={}
    ans=0
    for i in range(1,n):
        if i==1:
            if s[i]==s[0]:
                ans+=1
                d[i]=1
        else:
            if (s[i]==s[i-1] and i-1 not in d):
                ans+=1
                d[i]=1
            elif s[i]==s[i-2] and i-2 not in d:
                ans+=1
                d[i]=1
    print(ans)