t = int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=[]
    zstack=[]
    ostack=[]
    pans=0
    curr=0
    for i in range(n):
        if s[i]=='0':
            if len(ostack)==0:
                zstack.append(curr)
                ans.append(curr+1)
                curr+=1
            else:
                noice=ostack.pop()
                ans.append(noice+1)
                zstack.append(noice)
        else:
            if len(zstack)==0:
                ostack.append(curr)
                ans.append(curr+1)
                curr+=1
            else:
                noice=zstack.pop()
                ans.append(noice+1)
                ostack.append(noice)
        pans=max([pans,len(zstack),len(ostack)])
    print(pans)
    print(' '.join(list(map(str,ans))))

