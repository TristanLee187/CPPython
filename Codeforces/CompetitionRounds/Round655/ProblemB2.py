t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        print(n//2,n//2)
    else:
        thing = int(n**0.5)
        while n%thing!=0:
            thing-=1
        print(thing,n-thing)
        
    
    
