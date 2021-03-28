for _ in range(int(input())):
    p=int(input())
    l=[]
    for i in range(p):
        l.append(list(map(int,input().split())))
    l.sort()
    flag=True
    ans=''
    ans+=l[0][0]*'R'+l[0][1]*'U'
    for i in range(1,p):
        a=l[i][0]-l[i-1][0]
        b=l[i][1]-l[i-1][1]
        if a<0 or b<0:
            flag=False
            break
        ans+=a*'R'+b*'U'
    if flag:
        print('YES')
        print(ans)
    else:
        print('NO')