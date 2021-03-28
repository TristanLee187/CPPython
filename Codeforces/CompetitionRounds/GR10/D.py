t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    if s[-1]==s[0]:
        i=n-1
        while i>0 and s[i]==s[0]:
            i-=1
        if i!=0:
            s=s[i+1:]+s[:i+1]
    ans=0
    for i in range(n):
        if s[i]=='R':
            if not (s[(i+1)%n]=='L' or s[(i+2)%n]=='L'):
                ans+=1
                if s[(i+3)%n]=='R':
                    s[(i+2)%n]='L'
        else:
            if not (s[(i-1)%n]=='R' or s[(i-2)%n]=='R'):
                ans += 1
                s[i]='R'
    print(ans)


