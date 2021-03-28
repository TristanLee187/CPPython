for _ in range(int(input())):
    s=input()
    accs=[]
    ids=[]
    last=s[0]
    acc=1
    for i in range(1,len(s)):
        if s[i]==last:
            acc+=1
        else:
            ids.append(last)
            accs.append(acc)
            acc=1
            last=s[i]
    ids.append(last)
    accs.append(acc)
    i=1
    if ids[0]=='0':
        i=2
    ans=0
    while i<len(accs)-1:
        ans+=accs[i]
        i+=2
    print(ans)
