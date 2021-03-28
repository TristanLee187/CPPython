import math

t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    k=l[1]
    s=input()
    spaces=[]
    i=0
    found=False
    while i<n:
        if s[i]=='1':
            spaces.append(i)
            found=True
        i+=1
    if found:
        tspaces=[]
        i=1
        if spaces[0]!=0:
            tspaces.append(spaces[0])
        while i<len(spaces):
            tspaces.append(spaces[i]-spaces[i-1]-1)
            i+=1
        if spaces[-1]!=n-1:
            tspaces.append(n-1-spaces[-1])
        ans=0
        j=0
        while j<len(tspaces):
            if (j==0 and s[0]=='0') or (j==len(tspaces)-1 and s[-1]=='0'):
                ans+=math.ceil((tspaces[j]-k)/(k+1))
            else:
                ans+=math.ceil((tspaces[j]-2*k)/(k+1))
            j+=1
        print(ans)
    else:
        print(math.ceil(n/(k+1)))
    
            
            
    
