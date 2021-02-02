file = open('sort.in', 'r')
s=file.readline()
l=list(map(int, file.readline().split(' ')))
l=sorted(l)
file2 = open('sort.out', 'w')
for i in range(len(l)):
    if i==len(l)-1:
        file2.write(str(l[i]))
    else:
        file2.write(str(l[i])+' ')
file.close()
file2.close()
