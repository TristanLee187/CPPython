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
    n,m=rns()
    a=rl()
    b=rl()
    c=rl()
    diff={}
    same={}
    for i in range(n):
        if a[i]!=b[i]:
            if b[i] in diff:
                diff[b[i]].append(i)
            else:
                diff[b[i]]=[i]
        else:
            if b[i] in same:
                same[b[i]].append(i)
            else:
                same[b[i]]=[i]
    ans=True
    lans=[]
    done=set()
    for i in range(m-1,-1,-1):
        if c[i] in diff:
            if len(diff[c[i]])>1:
                lans.append(diff[c[i]].pop()+1)
            elif len(diff[c[i]])==1:
                lans.append(diff[c[i]][0]+1)
                done.add(c[i])
        elif c[i] not in diff:
            if len(lans)>0:
                lans.append(lans[-1])
            else:
                if c[i] in same:
                    lans.append(same[c[i]][0] + 1)
                else:
                    ans=False
        elif c[i] in same:
            lans.append(same[c[i]][0]+1)
        else:
            ans=False
    for i in diff:
        if i not in done:
            ans=False
            break
    if ans:
        YN(ans)
        print(*lans[::-1])
    else:
        YN(ans)