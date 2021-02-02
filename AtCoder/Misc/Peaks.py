i = input()
i = i.split(' ')
l = []
while len(l)<int(i[0]):
  l += [0]

lim = int(i[1])

i = input()
i = i.split(' ')
for j in list(range(len(l))):
    i[j]=int(i[j])


count=0
while count<lim:
    count += 1
    k = input()
    k = k.split(' ')
    if i[int(k[0])-1]==i[int(k[1])-1]:
        l[int(k[1])-1] = 1
        l[int(k[0])-1] = 1
    elif i[int(k[0])-1]>i[int(k[1])-1]:
        l[int(k[1])-1] = 1
    else:
        l[int(k[0])-1] = 1

count = 0
for j in l:
    if j==0:
        count += 1
print(count)
  
