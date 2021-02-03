n,k=map(int,input().split())
a=[]
for i in range(k):
    a.append(list(map(int,input().split())))
ans=(n+1)*[1]
paths={}
for i in range(1,n+1):
    paths[i]=[]
pos=list(range(n+1))
for l,r in a:
    paths[pos[l]].append(r)
    paths[pos[r]].append(l)
    pos[l],pos[r]=pos[r],pos[l]
#print(paths)
ans=[]
tr=[]
for i in range(1,n+1):
    if paths[i]==[]:
        ans.append(1)
        tr.append({})
    else:
        curr=i
        seenlast={i}
        seen=set([i]+paths[i])
        while paths[curr][-1] not in seenlast:
            if paths[curr][-1]-1<len(tr):
                for k in tr[paths[curr][-1]-1]:
                    seen.add(k)
                break
            seenlast.add(paths[curr][-1])
            for char in paths[paths[curr][-1]]:
                seen.add(char)
            curr=paths[curr][-1]
        ans.append(len(seen))
        tr.append(seen)
for i in ans:
    print(i)