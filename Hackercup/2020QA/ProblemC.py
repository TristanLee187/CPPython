import bisect

file=open('ans.txt', 'w')
file=open('timber_sample_input.txt', 'r')
t=int(file.readline())
for _ in range(t):
    n=int(file.readline())
    pos=[]
    his=[]
    for i in range(n):
        p,h=map(int,file.readline().split())
        pos.append(p)
        his.append(h)
    tpos=pos
    tpos=sorted(pos)
    this=[]
    this.extend(n*[0])
    for i in range(n):
        j=bisect.bisect_left(tpos,pos[i])
        this[j]=his[i]
    ans=-float('inf')
    point=tpos[0]
    curr=0
    for i in range(n):
        if tpos[i]==point or tpos[i]-this[i]==point:
            curr+=this[i]
            point+=this[i]
        else:
            ans=max(ans,curr)
            curr=this[i]
            point=tpos[i]+this[i]
    ans=max(curr,ans)
    print(tpos)
    print(this)
    print('Case #'+str(_+1)+': ' + str(ans))
        
    
    
