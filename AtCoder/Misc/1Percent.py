
t=int(input())
ans=0
start=100
while start<t:
    start += int(start/100)
    ans+=1
print(ans)
