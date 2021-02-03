t=int(input())
count=0
while count<t:
    count+=1
    n = int(input())
    l = list(map(int, input().split(' ')))
    c = []
    ans=True
    tcount=0
    for i in l:
        if tcount+i in c:
            ans=False
            break
        else:
            c+=[tcount+i]
        tcount+=1
    for i in l:
        if tcount+i in c:
            ans=False
            break
        else:
            c+=[tcount+i]
        tcount+=1
    if ans:
        print("YES")
    else:
        print("NO")
            
        
