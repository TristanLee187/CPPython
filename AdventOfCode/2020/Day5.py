ans=[]
for i in range(781):
    s=input()
    high=127
    low=0
    for j in range(7):
        from math import ceil

        mid=ceil((high+low)/2)
        if s[j]=='F':
            high=mid
        else:
            low=mid
    col=low
    high = 8
    low = 0
    for j in range(7,10):
        from math import ceil

        mid = ceil((high + low) / 2)
        if s[j] == 'L':
            high = mid
        else:
            low = mid
    row=low
    tans=8*col+row
    ans.append(tans)

ans.sort()
for i in range(1,len(ans)):
    if ans[i]-ans[i-1]==2:
        print(ans[i-1]+1)
print(ans)