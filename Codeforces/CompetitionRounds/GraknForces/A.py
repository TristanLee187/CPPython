rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')

for _ in range(rn()):
    n=int(input())
    a=rl()
    b=rl()
    c=rl()
    ans=[]
    ans.append(a[0])
    for i in range(1,n-1):
        d=[a[i],b[i],c[i]]
        for i in d:
            if i!=ans[-1]:
                ans.append(i)
                break
    d=[a[-1],b[-1],c[-1]]
    for i in d:
        if i!=ans[-1] and i!=ans[0] and n>1:
            ans.append(i)
            break
    print(' '.join(list(map(str,ans))))