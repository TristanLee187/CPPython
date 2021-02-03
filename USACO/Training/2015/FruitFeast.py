prob="feast"

file=open(prob+".in")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

#
#Read input
t,a,b=rns()
#
file.close()

#CODE
ans=0
dp=(t+1)*[False]
dp[0]=True
drink=(t+1)*[False]
for i in range(t+1):
    if dp[i]:
        if i+a<=t:
            dp[i+a]=True
            drink[(i+a)//2]=True
        if i+b<=t:
            dp[i+b]=True
            drink[(i+b)//2]=True
for i in range(t+1):
    if drink[i]:
        if i+a<=t:
            dp[i+a]=True
            drink[i+a]=True
        if i+b<=t:
            dp[i+b]=True
            drink[i+b]=True

for i in range(t,-1,-1):
    if dp[i]:
        ans=i
        break
#

file=open(prob+".out","w")
file.write(str(ans))
file.close()