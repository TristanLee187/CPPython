for _ in range(int(input())):
    n=int(input())
    d={}
    for i in range(n):
        s=input()
        for j in s:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
    ans=True
    for i in list(d.values()):
        if i%n!=0:
            ans=False
            break
    if ans:
        print('YES')
    else:
        print('NO')

