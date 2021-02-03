s=input()
t=input()
ans=float('inf')
for i in range(len(s)-len(t)+1):
    a=s[i:i+len(t)]
    tans=0
    for i in range(len(t)):
        tans+=(t[i]!=a[i])
    ans=min(ans,tans)
print(ans)