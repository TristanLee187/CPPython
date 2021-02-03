t=int(input())
for z in range(t):
    n,k = map(int, input().split(' '))
    if k%n==0:
        print(0)
    else:
        print(2)
    
    thing=k%n
    index = 0
    printlist=[]
    while index<n:
        if thing>0:
            thing-=1
            if index+k//n+1>n:
                printlist.append((index+k//n-n+1)*'1'+(n-k//n-1)*'0'+(n-index)*'1')
            else:
                printlist.append(index*'0'+(k//n+1)*'1'+(n-k//n-index-1)*'0')
        else:
            if index+k//n>n:
                printlist.append((index+k//n-n)*'1'+(n-k//n)*'0'+(n-index)*'1')
            else:
                printlist.append((index)*'0'+(k//n)*'1'+(n-k//n-index)*'0')
        index+=1

    if len(printlist)==0:
        print(0)
    for i in printlist:
        print(i)
            
        
    
    
