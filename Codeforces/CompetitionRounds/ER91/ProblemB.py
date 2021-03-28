t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    ans=''
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    a=list(d.keys())
    move=a[0]
    for i in d:
        if d[i]>d[move]:
            move=i
    if move=='R':
        move='P'
    elif move=='P':
        move='S'
    else:
        move='R'
    ans=n*move
    print(ans)
        
    
    
    
