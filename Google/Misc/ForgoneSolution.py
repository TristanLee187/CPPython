t = int(input())
for _ in range(t):
    n = input()
    a=''
    for i in n:
        if i=='4':
            a+='1'
        else:
            a+='0'
    a=int(a)
    b=int(n)-a
    ans=[a,b]

    print('Case #' + str(_ + 1) + ': ' + ' '.join(list(map(str,ans))))

