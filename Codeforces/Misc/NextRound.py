i = int(input().split(' ')[1])-1
j = list(map(int, input().split(' ')))
comp = j[i]
count = 0
for n in j:
    if n>=comp and n>0:
        count+=1
        
print(count)
