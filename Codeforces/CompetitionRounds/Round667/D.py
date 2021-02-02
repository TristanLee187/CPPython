for _ in range(int(input())):
    n,s=map(str,input().split())
    s=int(s)
    pow=-1
    su=0
    flag=True
    for i in n:
        su+=int(i)
        if su>s:
            flag=False
            break
        if i!=0:
            pow+=1
    if flag:
        print(0)
    else:
        if pow==-1:
            n='0'+n
        ans=n[:max(pow,0)]+str(int(n[pow+1])+1)+(len(n)-(pow==-1)-pow-1)*'0'
        print(ans,pow)
        print(int(ans)-int(n))

