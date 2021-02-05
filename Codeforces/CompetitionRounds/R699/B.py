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
    n,k=rns()
    h=rl()
    ans=[]
    while True:
        flag=False
        for i in range(n):
            if i==n-1:
                flag=True
                break
            if h[i]<h[i+1]:
                ans.append(i+1)
                h[i]+=1
                break
        if flag:
            break
    if k>len(ans):
        print(-1)
    else:
        print(ans[k-1])