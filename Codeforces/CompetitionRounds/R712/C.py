rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    c=s.count('1')
    if s[0]==s[-1]=='1' and c%2==0:
        print('YES')
        a=''
        b=''
        turn=1
        ones=0
        for i in range(n):
            if s[i]=='0':
                if turn==1:
                    a+='('
                    b+=')'
                else:
                    a+=')'
                    b+='('
                turn*=-1
            elif ones<c//2:
                a+='('
                b+='('
                ones+=1
            else:
                a+=')'
                b+=')'
        print(a)
        print(b)
    else:
        print('NO')