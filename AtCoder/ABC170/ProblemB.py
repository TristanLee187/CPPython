l=list(map(int, input().split(' ')))
a=l[0]
b=l[1]
if b>=2*a and b<=4*a and b%2==0:
    print("Yes")
else:
    print("No")
    
