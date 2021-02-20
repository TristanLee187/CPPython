rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

s=rs()
ans=True
for i in range(len(s)):
    if i%2==0:
        if s[i].lower()!=s[i]:
            ans=False
            break
    else:
        if s[i].upper()!=s[i]:
            ans=False
            break
yn(ans)