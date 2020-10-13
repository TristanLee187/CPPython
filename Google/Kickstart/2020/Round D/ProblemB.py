t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int, input().split(' ')))
    if n==1:
        print('Case #' + str(_+1)+': ' + str(0))
    else:
        diffs=[]
        for i in range(1,n):
            diff=l[i]-l[i-1]
            if diff==0:
                diffs.append(0)
            else:
                diffs.append(diff//abs(diff))

            

        ans=0
        b=0
        lb=0
        last=diffs[0]
        for i in diffs:
            if i!=0 and i!=last:
                lb=b
                last=i
            b+=i
            if abs(lb-b)==4:
                ans+=1
                lb=b
            
        print('Case #' + str(_+1)+': ' + str(ans))
        
