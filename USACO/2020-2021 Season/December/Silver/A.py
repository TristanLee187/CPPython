n=int(input())
if n>1:
    d={}
    for i in range(n-1):
        j=sorted((list(map(int,input().split()))))
        if j[0] in d:
            d[j[0]][j[1]]=1
        else:
            d[j[0]]={j[1]:1}
        if j[1] in d:
            d[j[1]][j[0]]=1
        else:
            d[j[1]]={j[0]:1}
    from math import log
    from math import ceil
    def bfs(d,key,done):
        done[key]=True
        tkey=0
        ans=0
        for k in d[key]:
            if not done[k]:
                tkey+=1
                ans+=bfs(d,k,done)
        if tkey>0:
            ans+=ceil(log(tkey+1, 2)) + tkey
        return ans
    done=(10**5+1)*[False]
    print(bfs(d,1,done))
else:
    print(0)