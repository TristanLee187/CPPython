t=int(input())
count=0
while count<t:
    count+=1
    n=int(input())
    l=list(map(int, input().split(' ')))
    l=sorted(l)
    num=1
    i=0
    while i<n:
        if num>=l[i]:
            num+=1
            i+=1
        elif i==n-1:
            break
        else:
            test=i
            for j in range(test+1,n):
                if j+1>=l[j]:
                    num+=j-test+1
                    i=j+1
                    break
                i+=1
                
                
    print(num)

                
