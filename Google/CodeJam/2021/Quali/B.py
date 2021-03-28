rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    ans=0

    x,y,s=input().split()
    x,y=int(x),int(y)

    i=0
    while i<len(s):
        if s[i]=='?':
            j=i
            while j<len(s) and s[j]=='?':
                j+=1
            if i==0 or j==len(s) or s[i]==s[j]:
                ans+=0
            elif s[j]=='J':
                ans+=x*int(s[i-1]=='C')
            else:
                ans+=y*int(s[i-1]=='J')
            i=j-1
        elif s[i]=='C' and i+1<len(s) and s[i+1]=='J':
            ans+=x
        elif s[i]=='J' and i+1<len(s) and s[i+1]=='C':
            ans+=y
        i+=1
    print('Case #' + str(_+1)+': ' + str(ans))