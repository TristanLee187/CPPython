for _ in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    queries=[]
    for i in range(q):
        queries.append(list(map(int,input().split())))
    pre=[26*[0]]
    for i in s:
        pre.append(pre[-1].copy())
        pre[-1][ord(i)-65]+=1
    ans=0
    for i in queries:
        a=pre[i[0]-1]
        b=pre[i[1]]
        c=[b[j]-a[j] for j in range(26)]
        if (i[1]-i[0]+1)%2==0:
            ans+=int(all([i%2==0 for i in c]))
        else:
            ans+=int(len([i for i in c if i%2==1])==1)
    print('Case #' + str(_ + 1) + ': ' + str(ans))

