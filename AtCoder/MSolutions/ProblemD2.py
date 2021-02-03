n=int(input())
l=list(map(int,input().split()))
tl=[l[0]]
for i in range(1,n):
    if l[i]!=l[i-1]:
        tl.append(l[i])


a=[]
ma=False

for i in range(len(tl)):
    if i==0:
        if tl[i]>tl[i+1]:
            ma=True
            a.append(tl[i])
        else:
            ma=False
            a.append(tl[i])
    elif i==len(tl)-1:
        if tl[i]>tl[i-1]:
            a.append(tl[i])
        else:
            a.append(tl[i])
    else:
        if tl[i-1]<tl[i] and tl[i+1]<tl[i]:
            a.append(tl[i])
        elif tl[i-1]>tl[i] and tl[i+1]>tl[i]:
            a.append(tl[i])

if ma:
    a.pop(0)


num=0
ans=1000

for i in range(0,len(a)-1,2):
    thing1=(ans//a[i])*a[i+1]
    thing2=num*a[i+1]
    if thing1>thing2:
        ans=thing1+ans%a[i]
        num=0
        
    elif thing2>thing1:
        ans=thing2

print(ans)
        
            
            
        

    
