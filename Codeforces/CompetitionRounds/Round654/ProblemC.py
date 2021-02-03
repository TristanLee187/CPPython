t=int(input())
for i in range(t):
    a,b,n,m = map(int, input().split(' '))
    if n+m>a+b:
        print('No')
    else:
        if b<a:
            b-=m
            if b<0:
                print("No")
            else:
                print("Yes")
        else:
            a-=m
            if a<0:
                print("No")
            else:
                print("Yes")

        
