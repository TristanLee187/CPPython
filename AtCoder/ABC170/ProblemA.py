l=list(map(int, input().split(' ')))
ans=0
for i in range(len(l)):
    if l[i]==0:
        print(ans+1)
        break
    else:
        ans+=1
