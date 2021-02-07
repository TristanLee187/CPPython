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
    s=rs()
    ans=[]
    for i in range(len(s)):
        if i%2==0:
            if s[i]=='a':
                ans.append('b')
            else:
                ans.append('a')
        else:
            if s[i]=='z':
                ans.append('y')
            else:
                ans.append('z')
    print(''.join(ans))