file=open('ans.txt','w')
t=int(input())
for _ in range(t):
    n=int(input())
    i=input()
    o=input()

    ans=[]
    for j in range(n):
        ans.append([])
    
    def solve(s1,s2,x):
        if len(ans[x])>0:
            return ans[x]
        else:
            if s2[x]=='N':
                ans[x]=[x]
                return [x]
            else:
                thing=[]
                if x>0 and s1[x-1]=='Y':
                    thing=ans[x-1]
                if x==n-1 or s1[x+1]=='N':
                    ans[x] = thing+[x]
                    return ans[x]
                else:
                    ans[x] = thing+[x]
                    ans[x] += solve(s1,s2,x+1)
                    return ans[x]
                            

    for j in range(n):
        solve(i,o,j)

    pans=[]
    for j in ans:
        aans=[]
        for k in range(n):
            aans.append([0])
        for k in j:
            aans[k]=1
        attach=''
        for k in aans:
            if k==1:
                attach=attach+'Y'
            else:
                attach=attach+'N'
        pans.append(attach)

    file.write('Case #'+str(_+1)+':'+'\n')
    for j in pans:
        file.write(j+'\n')

file.close()
    
