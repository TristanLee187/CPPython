x = int(input())
l = input().split(' ')

count = 0


for i in list(range(len(l)-1)):
    for j in list(range(i,len(l))):
        if abs(i-j)==int(l[i])+int(l[j]):
            count += 1

print(count)
