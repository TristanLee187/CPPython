a=[]
for i in range(323):
    a.append(input())
ans=0
right=1
for i in range(2,323,2):
    if a[i][right]=='#':
        ans+=1
    right+=1
    right%=len(a[i])
print(ans)