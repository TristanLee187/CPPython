rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,k=rns()
a=[]
for i in range(k):
    a.append(rl())
d={}
for i in a:
    if i[0] in d:
        d[i[0]].append(i[1])
    else:
        d[i[0]]=[i[1]]
    if i[1] in d:
        d[i[1]].append(i[0])
    else:
        d[i[1]]=[i[0]]
a={}
for i in d:
    a[i]=(10**5+1)*[0]
    for j in range(len(d[i])):
        if j==len(d[i])-1:
            a[i][d[i][j]]=-1
        else:
            a[i][d[i][j]]=d[i][j+1]

paths={}
for i in range(1,n+1):
    paths[i]=[]
    if i in d:
        curr=i
        next=d[i][0]
        paths[i]+=[curr,next]
        while a[next][curr]!=-1:
            paths[i].append(a[next][curr])
            curr,next = next,a[next][curr]


ans=[]
for i in range(1,n+1):
    if paths[i]==[]:
        ans.append(1)
    else:
        curr=i
        seenl=set([i])
        seen=set(paths[i])
        while paths[curr][-1] not in seenl:
            seenl.add(paths[curr][-1])
            seen=set(list(seen)+paths[paths[curr][-1]])
            curr=paths[curr][-1]
        ans.append(len(seen))

for i in ans:
    print(i)