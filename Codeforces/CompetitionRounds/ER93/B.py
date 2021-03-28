t = int(input())
for _ in range(t):
    s=input()
    ids=[]
    acc=[]
    a=s[0]
    c=1
    for i in s[1:]:
        if i==a:
            c+=1
        else:
            ids.append(a)
            acc.append(c)
            a=i
            c=1
    ids.append(a)
    acc.append(c)
    taccs=[]
    for i in range(len(ids)):
        if ids[i]=='1':
            taccs.append(acc[i])
    taccs=sorted(taccs)[::-1]
    ans=0
    for i in range(0,len(taccs),2):
        ans+=taccs[i]
    print(ans)
