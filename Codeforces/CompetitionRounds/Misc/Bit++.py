i = int(input())
count=0
x=0
while count<i:
    read = (input())[1]
    if read=='+':
        x+=1
    else:
        x-=1
    count+=1
print(x)
