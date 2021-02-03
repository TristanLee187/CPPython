rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n,q=rns()
    vals=rs()
    acc=[0]
    val=0
    mm=[0,0]
    pre=[[0,0]]
    for i in vals:
        if i=='-':
            val-=1
        else:
            val+=1
        acc.append(val)
        mm[0]=min(mm[0],val)
        mm[1]=max(mm[1],val)
        pre.append(mm.copy())
    val=0
    mm=[0,0]
    suff=[[0,0]]
    for i in vals[::-1]:
        if i=='-':
            val-=1
        else:
            val+=1
        mm[0]=min(mm[0],val)
        mm[1]=max(mm[1],val)
        suff.append(mm.copy())
    suff=suff[::-1]
    for i in range(q):
        query=rl()
        range1=pre[query[0]-1].copy()
        delta=acc[query[1]-1]
        range2=suff[query[1]].copy()
        range2[0]+=delta
        range2[1]+=delta

        ans=range1[1]-range1[0]+range2[1]-range2[0]+2
        if query[1]==n:
            ans=range1[1]-range1[0]+1
        if range1[0]<=range2[0] and range2[1]<=range1[1]:
            ans-=range2[1]-range2[0]+1
        elif range2[0]<=range1[0] and range1[1]<=range2[1]:
            ans-=range1[1]-range1[0]+1
        elif range2[0]<=range1[1] and range1[0]<range2[0] and range2[1]>range1[1]:
            ans-=range1[1]-range2[0]+1
        elif range1[0]<=range2[1] and range1[1]>range2[1] and range2[0]<range1[0]:
            ans -= range2[1] - range1[0] + 1

        print(range1,range2, ans)
    print(pre)
    print(suff)
    print(acc)