rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    d=rl()
    dic={}
    for i in d:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    ans=True
    for i in dic:
        if dic[i]!=2:
            ans=False
            break
    if not ans:
        print('NO')
    else:
        l=sorted(list(dic.keys()),reverse=True)
        pre=0
        if l[0]%(2*n)!=0:
            ans=False
        pre+=(l[0]//(2*n))
        last=(l[0]//(2*n))
        lasts=[last]
        for i in range(1,n):
            if (l[i]-(2*pre))%(2*n-2*i)==0 and 0<(l[i]-(2*pre))//(2*n-2*i)<=last:
                last = (l[i] - (2 * pre)) // (2 * n - 2 * i)
                lasts.append(last)
                pre += (l[i] - (2 * pre)) // (2 * n - 2 * i)
            else:
                ans=False
                break
        YN(ans)