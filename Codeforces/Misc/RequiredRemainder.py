t=int(input())
for i in range(t):
    x,y,n = map(int, input().split(' '))
    if n<x:
        print(y)
    else:
        thing=n%x
        if thing==y:
            print(n)
        else:
            if thing>y:
                thing-=y
            else:
                thing+=(x-y)
            print(n-thing)
            
