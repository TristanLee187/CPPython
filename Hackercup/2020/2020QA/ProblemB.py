file=open('ans.txt', 'w')
filer=open('alchemy_input.txt', 'r')
t=int(filer.readline())
for _ in range(t):
    n=int(filer.readline())
    s=filer.readline().strip()

    a=0
    b=0
    for i in range(n):
        if s[i]=='A':
            a+=1
        else:
            b+=1
    file.write('Case #' + str(_+1)+': ')
    if abs(b-a)==1:
        file.write('Y\n')
    else:
        file.write('N\n')

file.close()
filer.close()
    
        
