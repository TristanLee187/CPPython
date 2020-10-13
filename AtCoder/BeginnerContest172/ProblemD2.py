n=int(input())
ans=1

l=range(2, n+1)

while len(l)>0:
    index=0
    thing=1
    while thing<=n:
        ans+=l[index]*(index+1)
        thing*=l[index]
        index+=1

print(ans)
    
    
