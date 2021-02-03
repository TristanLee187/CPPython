t = int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)

    ans=0
    for k in range(n,-1,-1):
        for i in range(k,0,-1):
            d={}
            for j in range(i//2):
                s=l[j]+l[i-j-1]
                if s in d:
                    d[s]+=1
                else:
                    d[s]=1
            ans=max([ans]+list(d.values()))
    print(ans)


