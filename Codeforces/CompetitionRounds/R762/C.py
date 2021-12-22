from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    a,s=rs().split()
    sp=len(s)-1
    np=len(a)-1
    pans=True
    ans=''
    while sp>=0 or np>=0:
        if np>=0 and sp<0:
            pans=False
            break
        elif np<0 and sp>=0:
            ans+=s[sp]
            sp-=1
        elif int(s[sp])>=int(a[np]):
            ans+=str(int(s[sp])-int(a[np]))
            sp-=1
            np-=1
        elif sp>0 and int(s[sp-1:sp+1])>=int(a[np]) and int(s[sp-1:sp+1])-int(a[np])<10:
            ans+=str(int(s[sp-1:sp+1])-int(a[np]))
            sp-=2
            np-=1
        else:
            pans=False
            break
    if pans:
        print(int(ans[::-1]))
    else:
        print(-1)