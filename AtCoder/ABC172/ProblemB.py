s=input()
t=input()
ans=0
for i in range(len(s)):
    if t[i]!=s[i]:
        ans+=1
print(ans)
