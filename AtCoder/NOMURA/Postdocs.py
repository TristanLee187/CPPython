string = input()
ans=''
for i in string:
    if i=='P' or i=='D':
        ans+=i
    else:
        ans+='D'
print(ans)
