rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    a,b=rns()
    s=rs()
    if len(s)==0:
        print(0)
    else:
        ids=[s[0]]
        accs=[0]
        for i in s:
            if i==ids[-1]:
                accs[-1]+=1
            else:
                ids.append(i)
                accs.append(1)
        ans=0
        for i in range(len(ids)):
            if ids[i]=='0' and i>0 and i<len(ids)-1:
                if a>b*accs[i]:
                    ans+=b*accs[i]
                    ids[i]='1'
        for i in range(len(ids)):
            if ids[i]=='1':
                if i==0:
                    ans+=a
                elif i>0 and len(ids)>1 and ids[i-1]=='0':
                    ans+=a
                elif len(ids)==1:
                    ans+=a
        print(ans)
