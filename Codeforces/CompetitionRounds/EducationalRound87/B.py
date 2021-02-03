t=int(input())
for _ in range(t):
    s=input()
    ids=[]
    acc=[]
    curr=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            pass
        else:
            ids.append(s[i-1])
            acc.append(curr)
            curr=0
        curr+=1
    ids.append(s[-1])
    acc.append(curr)
    ans=float('inf')
    for i in range(1,len(ids)-1):
        if len(list(set([ids[i-1],ids[i],ids[i+1]])))==3:
            ans=min(ans,acc[i]+2)
    if ans==float('inf'):
        print(0)
    else:
        print(ans)