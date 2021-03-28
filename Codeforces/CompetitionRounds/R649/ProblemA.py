t=int(input())
for z in range(t):
    n,x = map(int,input().split(' '))
    l=list(map(int, input().split(' ')))
    if sum(l)%x!=0:
        print(n)
    else:
        thing1=0
        thing2=0
        for i in l:
            thing1+=1
            if i!=0 and i%x!=0:
                break
        for i in l[::-1]:
            thing2+=1
            if i!=0 and i%x!=0:
                break

        if min(thing1, thing2)==n:
            print(-1)
        else:
            print(n - min(thing1, thing2))
        
    
