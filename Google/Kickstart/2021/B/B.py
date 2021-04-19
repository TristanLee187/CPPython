from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

for _ in range(rn()):
    n=rn()
    a=rl()
    diff=[a[i]-a[i-1] for i in range(1,n)]
    acc=[1]
    for i in range(1,n-1):
        if diff[i]==diff[i-1]:
            acc.append(acc[-1]+1)
        else:
            acc.append(1)
    for i in range(n-2,0,-1):
        if diff[i]==diff[i-1]:
            acc[i-1]=acc[i]
    ans=max(acc)+1
    for i in range(n):
        if i==0:
            if acc[0]==1 and len(acc)>1:
                ans=max(ans,acc[1]+2)
        elif i==n-1:
            if acc[-1]==1 and len(acc)>1:
                ans=max(ans,acc[-2]+2)
        else:
            j=i-1
            con=[]
            if j>0 and diff[j]!=diff[j-1]:
                con.append(acc[j-1]+1)
            if j<len(acc)-2 and diff[j+1]!=diff[j+2]:
                con.append(acc[j+2]+1)
            if j>0 and (diff[j]-diff[j-1]==diff[j-1]-diff[j+1]) and diff[j]!=diff[j+1]:
                con.append(acc[j-1]+2)
                if j<len(acc)-2 and diff[j+2]==diff[j-1]:
                    con[-1]+=acc[j+2]
            if j>0 and (diff[j+1]-diff[j-1]==diff[j]-diff[j+1]) and diff[j]!=diff[j-1]:
                con.append(acc[j+1]+2)
            if len(con)>0:
                ans=max(ans,max(con)+1)
    print('Case #' + str(_+1)+': ' + str(ans))