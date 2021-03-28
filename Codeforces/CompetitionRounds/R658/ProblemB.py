t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    if sum(l)==n:
        if n%2==0:
            print('Second')
        else:
            print('First')
    else:
        i=1
        while i<n and l[i-1]==1:
            i+=1
        if i%2==0:
            print('Second')
        else:
            print('First')
            

    

    

    
