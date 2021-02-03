d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']



t=int(input())
for _ in range(t):
    n=int(input())
    s1=input()
    s2=input()

    ans=0
    used=[]
    for i in range(400):
        used.append(0)
        
    
    for i in range(n):
        if s2[i]<s1[i]:
            ans=-1
            break
        else:
            index = d.index(s1[i])*20+d.index(s2[i])
            used[index]+=1
            
    for i in range(len(used)):
        if used[i]!=0:
            ans+=1
            val=used[i]
            
    
    
    
