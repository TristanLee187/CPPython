rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=[]
    for i in range(n):
        l.append(input())
    if l[0][1]==l[1][0]:
        res=0
        ans=[]
        if l[-1][-2]==l[0][1]:
            ans.append([n,n-1])
            res+=1
        if l[-2][-1]==l[0][1]:
            ans.append([n-1,n])
            res+=1
        print(res)
        for i in ans:
            print(*i)
    elif l[-1][-2]==l[-2][-1]:
        res = 0
        ans = []
        if l[-1][-2] == l[0][1]:
            ans.append([1,2])
            res += 1
        if l[-2][-1] == l[1][0]:
            ans.append([2,1])
            res += 1
        print(res)
        for i in ans:
            print(*i)
    else:
        print(2)
        print(2,1)
        if l[-1][-2]==l[0][1]:
            print(n,n-1)
        else:
            print(n-1,n)




