rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    if len(set(l))==1:
        print('NO')
    else:
        for i in range(n):
            l[i]=[l[i],i+1]
        l.sort()
        i=0
        while l[i][0]==l[0][0]:
            i+=1
        print('YES')
        for j in range(i,n):
            print(l[0][1],l[j][1])
        for j in range(1,i):
            print(l[j][1],l[i][1])