n=int(input())
easts=[]
norths=[]
for i in range(n):
    b=input().split()
    b[1]=int(b[1])
    b[2]=int(b[2])
    b=[b[1],b[2],i,b[0]]
    if b[-1]=='E':
        easts.append(b)
    else:
        norths.append(b)
easts.sort(key=lambda x:x[1])
norths.sort(key=lambda x:x[0])
blocks={}
tans={i:[] for i in range(n)}
for i in range(len(norths)):
    north=norths[i]
    for j in range(len(easts)):
        east=easts[j]
        if north[0]>east[0] and north[1]<east[1] and j not in blocks:
            left=north[0]-east[0]
            up=-(north[1]-east[1])
            if left<up:
                tans[east[2]]+=[north[2]]
                #print(str(east[2])+' blocked '+str(north[2]))
                break
            elif up<left:
                blocks[j]=False
                tans[north[2]]+=[east[2]]
                #print(str(north[2]) + ' blocked ' + str(east[2]))

blocks={}
for i in range(len(easts)):
    east=easts[i]
    for j in range(len(norths)):
        north=norths[j]
        if north[0]>east[0] and north[1]<east[1] and j not in blocks:
            left=north[0]-east[0]
            up=-(north[1]-east[1])
            if left>up:
                tans[north[2]]+=[east[2]]
                #print(str(north[2]) + ' blocked ' + str(east[2]))
                break
            elif up>left:
                blocks[j]=False
                tans[east[2]]+=[north[2]]
                #print(str(east[2]) + ' blocked ' + str(north[2]))
def dfs(tans,i):
    ans=len(set(tans[i]))
    for j in set(tans[i]):
        ans+=dfs(tans,j)
    return ans
for i in tans:
    print(dfs(tans,i))