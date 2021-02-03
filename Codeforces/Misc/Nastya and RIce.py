import math

t=int(input())
count=0
while count<t:
    count+=1
    vals = input()
    vals = vals.split(' ')
    for i in list(range(len(vals))):
        vals[i] = int(vals[i])

    b = abs(vals[0]*vals[1]-vals[3])<=vals[0]*vals[2]+vals[4]

    if b:
        print("YES")
    else:
        print("NO")

    
    
    
