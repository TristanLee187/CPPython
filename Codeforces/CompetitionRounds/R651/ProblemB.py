t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    l=list(map(int, input().split(' ')))
    i=0
    es=[]
    os=[]
    while i<2*n:
        if l[i]%2==0:
            es.append(i)
        else:
            os.append(i)
        i+=1
    
    left=len(es)%2
    if len(es)==0:
        i=0
        while i<len(os)-3:
            print(str(os[i]+1)+' '+str(os[i+1]+1))
            i+=2
    elif len(os)==0:
        i=0
        while i<len(es)-3:
            print(str(es[i]+1)+' '+str(es[i+1]+1))
            i+=2
    elif left==0:
        i=0
        while i<len(es)-1:
            print(str(es[i]+1)+' '+str(es[i+1]+1))
            i+=2
        i=0
        while i<len(os)-3:
            print(str(os[i]+1)+' '+str(os[i+1]+1))
            i+=2
    else:
        i=0
        while i<len(es)-2:
            print(str(es[i]+1)+' '+str(es[i+1]+1))
            i+=2
        i=0
        while i<len(os)-2:
            print(str(os[i]+1)+' '+str(os[i+1]+1))
            i+=2
        
        
    
        
    
            
            
        
        
    
            
    
