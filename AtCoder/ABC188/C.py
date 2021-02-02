rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
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
n=rn()
l=rl()
b=[]
for i in range(2**n):
    b.append([l[i],i+1])
while len(b)>2:
    a=[]
    for i in range(0,len(b),2):
        if b[i][0]>b[i+1][0]:
            a.append(b[i])
        else:
            a.append(b[i+1])
    b=a.copy()
b.sort()
print(b[0][1])