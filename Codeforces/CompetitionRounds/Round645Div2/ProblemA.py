t = int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n=l[0]
    m=l[1]
    if n%2==0 or m%2==0:
        print(int(m*n/2))
    else:
        print(n*int(m/2)+int(n/2+1))
        
    
    
