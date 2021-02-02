i = input()
l = []
for j in i:
    if j!='+':
        l+=[int(j)]
l = sorted(l)
for j in l[:len(l)-1]:
    print(j, end='+')
print(l[-1], end=' ')
