t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    if n%4!=0:
        print("NO")
    else:
        print("YES")
        k=2
        while k<=n:
            print(k,end=' ')
            k+=2
        k=1
        while k<n-2:
            print(k,end=' ')
            k+=2
        print(int(k+n/2))
        
