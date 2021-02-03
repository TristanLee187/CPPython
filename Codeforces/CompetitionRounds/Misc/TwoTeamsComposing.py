t=int(input())
count=0
while count<t:
    count+=1
    n= int(input())
    l = list(map(int, input().split(' ')))
    l = sorted(l)
    prev=l[0]
    tcount=1
    champ=1
    acc=0
    for i in l:
        if i==prev:
            acc+=1
        else:
            tcount+=1
            prev=i
            champ = max(champ,acc)
            acc=1
    champ = max(champ,acc)

    if n==1:
        print(0)
    elif l[0]==l[-1]:
        print(1)
    else:
        print(max(min(tcount-1,champ), min(tcount, champ-1)))
    
    
