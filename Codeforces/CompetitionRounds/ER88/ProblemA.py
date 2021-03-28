t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    m=l[1]
    k=l[2]
    per = n/k
    M = min(per, m)
    m-=M
    if m==0:
        print(int(M))
    elif m%(k-1)==0:
        print(int(M-m/(k-1)))
    else:
        print(int(M-int(m/(k-1))-1))
    
    
    
    
    
    
    
    
    
