rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

for _ in range(rn()):
    a,b=rns()
    one=min(b-1,a-2)
    tone=one
    if one==0:
        print(0)
    else:
        pair=[one+2,one+1]
        og=one+2
        ans=one
        while pair[0]+og<=a and pair[0]%pair[1]!=0:
            one-=1
            ans+=one
            pair[0]+=og
        pair[0]+=og
        sub=pair[0]//og
        add=pair[1]
        while pair[0]>a:
            add-=1
            pair[0]-=sub
        ans+=add-pair[1]
        print(ans)