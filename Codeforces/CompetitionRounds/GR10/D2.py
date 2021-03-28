t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ids=[]
    accs=[]
    last=s[0]
    a=1
    for i in range(1,n):
        if s[i]==last:
            a+=1
        else:
            ids.append(last)
            accs.append(a)
            a=1
        last=s[i]
    ids.append(last)
    accs.append(a)
    if len(ids)==1:
        print(accs[0]//2)
    else:
        for i in range(len(ids)):
            if ids[i]=='R' and ids[(i+1)%len(ids)]=='L':
                accs[i]-=1
                accs[(i+1)%len(ids)]-=1
        if ids[-1]==ids[0]:
            accs[0]+=accs.pop()
            ids.pop()
        ans=0
        for i in accs:
            ans+=i//2
        print(ans)