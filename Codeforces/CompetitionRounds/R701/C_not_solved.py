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
        #print(pair)
        og=one+2
        ans=one
        while pair[0]+og<=a and pair[0]%pair[1]!=0:
            one-=1
            ans+=one
            pair[0]+=og
        print(ans)