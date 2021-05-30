from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m=rns()
    s=list(rs())
    ids=[s[0]]
    accs=[1]
    one='1' in s
    for i in range(1,n):
        if s[i]==ids[-1]:
            accs[-1]+=1
        else:
            ids.append(s[i])
            accs.append(1)

    ans=[]
    for i in range(len(ids)):
        if ids[i]=='1':
            ans+=accs[i]*[ids[i]]
        elif not one:
            ans+=accs[i]*ids[i]
        elif i==0:
            add=min(accs[i],m)*[1]
            if len(add)<accs[i]:
                add+=(accs[i]-len(add))*[0]
            ans+=add[::-1]
        elif i==len(ids)-1:
            add = min(accs[i], m) * [1]
            if len(add) < accs[i]:
                add += (accs[i] - len(add)) * [0]
            ans += add
        else:
            if accs[i]==2:
                ans+=2*[1]
            else:
                border=min((accs[i])//2,m)
                mid = accs[i]-2*border
                add=border*[1]+mid*[0]+border*[1]
                ans+=add
    for i in ans:
        print(i,end='')
    print()

