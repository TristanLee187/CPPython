import math
n=int(input())
ans=n*[0]
count=1
while count<=6 and count<n:
    ans[count-1]=0
    count+=1
    if count==6:
        ans[count-1]=1
        count+=1

root=4
found=False
while not found:
    thing=math.ceil(int(root/3))
    while thing>0:
        s=root-thing
        a=int(s/2)
        b=s-a
        firstindex=root**2-(thing*a+a*b+thing*b)
        if firstindex>n:
            found=True
            break
        while a>=1 and b>=1:
            ways=len(set([thing,a,b]))
            index=root**2-(thing*a+a*b+thing*b)
            if index<=n:
                if ways==1:
                    ans[index-1]+=1    
                elif ways==2:
                    ans[index-1]+=3
                else:
                    ans[index-1]+=6
                if a<b:
                    a-=1
                    b+=1
                else:
                    a+=1
                    b-=1
            else:
                break
        thing-=1
    root+=1

for i in range(n):
    print(ans[i])
        
                
    
    
    
    
