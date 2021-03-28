t = int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    e=0
    o=0
    for i in l:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e>=3:
        print('Yes')
    else:
        if l[:3].count(0)>0:
            print('No')
        else:
            for i in l[:3]:
                if i%2==0:
                    e-=1
                    o+=1
                else:
                    o-=1
                    e+=1
            if l[3]%2==0:
                e-=1
                o+=1
            else:
                e+=1
                o-=1
            if e>=3:
                print('Yes')
            else:
                print('No')
