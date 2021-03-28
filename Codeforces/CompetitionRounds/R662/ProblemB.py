n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

fours=0
twos=0
for i in d.values():
    if i>=4:
        fours+=i//4
        twos+=(i%4)//2
    elif i>=2:
        twos+=1


e=int(input())
for i in range(e):
    [m,p]=input().split()
    p=int(p)
    if m=='+':
        if p in d:
            if d[p]==1:
                twos+=1
            elif d[p]==3:
                fours+=1
                twos-=1
            elif d[p]>4 and d[p]%4==3:
                fours+=1
                twos-=1
            elif d[p]>4 and d[p]%2==1:
                twos+=1
            d[p]+=1
        else:
            d[p]=1
    else:
        if d[p]>5 and d[p]%4==0:
            fours-=1
            twos+=1
        elif d[p]>5 and d[p]%2==0:
            twos-=1
        elif d[p]==4:
            fours-=1
            twos+=1
        elif d[p]==2:
            twos-=1
        d[p]-=1
    if fours>0 and (2*(fours-1)+twos)>=2:
        print('YES')
    else:
        print('NO')




