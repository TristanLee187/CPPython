import gc

t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    m=l[1]
    i=0
    l=[]
    while i<n:
        l.append(list(input().split(' ')))
        i+=1
    availRows=0
    availCols=0
    for i in range(n):
        if '1' not in l[i]:
            availRows+=1
    for i in range(m):
        ans=True
        for j in l:
            if j[i]=='1':
                ans=False
                break
        if ans:
            availCols+=1

            
    x = min(availRows, availCols)

    if x%2==0:
        print('Vivek')
    else:
        print('Ashish')
    
    
        
    
    
    
    
