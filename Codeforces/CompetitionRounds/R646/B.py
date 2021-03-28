t=int(input())
count=0
while count<t:
    count+=1
    string = input()
    vals=[]
    currentSum = 0
    lastVal = string[0]
    for i in string:
        if i==lastVal:
            currentSum+=1
        else:
            vals.append(currentSum)
            currentSum=1
            lastVal=i
    vals.append(currentSum)

    sums=[]

    for i in range(len(vals)):
        maybe=0
        for j in range(i,-1, -2):
            maybe += vals[j]
        maybe1 = maybe
        maybe2 = maybe
        for j in range(i+2, len(vals), 2):
            maybe1 += vals[j]
        for j in range(i+3, len(vals), 2):
            maybe2 += vals[j]
        sums.append(min(maybe1, maybe2))

    
    

    if len(vals)<3:
        print(0)
    else:
        print(min(sums))
    
            
    
    
