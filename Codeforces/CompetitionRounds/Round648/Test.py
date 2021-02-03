l = open('test.txt', 'w')
l.write(str(int(2*10**5)))
l.write('\n')
for i in range(1, 2*10**5+1):
    l.write(str(i))
    l.write(' ')
for i in range(1, 2*10**5+1):
    l.write(str(i))
    l.write(' ')

l.close()
