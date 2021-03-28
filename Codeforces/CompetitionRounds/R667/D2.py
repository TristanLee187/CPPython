for _ in range(int(input())):
    n,s=map(str,input().split())
    s=int(s)
    l=[0,int(n[0])]
    for i in range(1,len(n)):
        l.append(l[-1]+int(n[i]))
        if l[-1]>s:
            break
    if l[-1]<=s:
        print(0)
    else:
        i=len(l)-1
        while l[i]>=s:
            i-=1
        if i==0:
            thing=1
        else:
            thing=int(n[:i])+1
        thing*=10**(len(n)-i)
        print(thing-int(n))


