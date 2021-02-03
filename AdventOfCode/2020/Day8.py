a=[]
for i in range(625):
    b=input().split()
    b[1]=int(b[1])
    a.append(b)
def execute(a):
    index=0
    d=[]
    for i in range(625):
        d.append(0)
    acc=0
    while index<625 and d[index]==0:
        d[index] = 1
        if a[index][0]=='acc':
            acc+=a[index][1]
            index+=1
        elif a[index][0]=='jmp':
            index+=a[index][1]
        else:
            index+=1
    if index==625:
        print(acc)

execute(a)
for i in range(625):
    if a[i][0]=='nop':
        a[i][0]='jmp'
        execute(a)
        a[i][0]='nop'
    elif a[i][0]=='jmp':
        a[i][0]='nop'
        execute(a)
        a[i][0]='jmp'