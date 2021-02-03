t=int(input())
count=0
while count<t:
    count+=1
    n = int(input())
    if n<3:
        print(0)
    elif n%2==0:
        print(n//2-1)
    else:
        print(n//2)
