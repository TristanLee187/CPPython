rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b=rns()
    s=list(rs())
    n=a+b
    flag=a%2+b%2<2
    for i in range(n):
        if s[i] in ['0','1']:
            if s[i]=='0':
                a-=1
            else:
                b-=1
            if s[-(1+i)]=='?':
                s[-(1 + i)] = s[i]
                if i>=n//2 and n%2==0 or (i>n//2 and n%2==1):
                    if s[i] == '0':
                        a -= 1
                    else:
                        b -= 1
            elif s[-(1+i)]!=s[i]:
                flag=False
                break
    if not flag:
        print(-1)
    elif s.count('?')%2==0:
        if (a%2==1 or b%2==1):
            print(-1)
        else:
            for i in range(n):
                if s[i]=='?':
                    if a>0:
                        a-=2
                        s[i] = s[-(i+1)] = '0'
                    else:
                        b-=2
                        s[i] = s[-(i+1)] = '1'
            if '?' in s or a<0 or b<0:
                print(-1)
            else:
                print(''.join(s))
    elif s.count('?')%2==1:
        if a%2==0 and b%2==0 and s[n//2]!='?':
            print(-1)
        else:
            for i in range(n):
                if i==n//2:
                    if a%2==1:
                        a-=1
                        s[i]='0'
                    else:
                        b-=1
                        s[i]='1'
                if s[i] == '?':
                    if a > 1:
                        a -= 2
                        s[i] = s[-(i + 1)] = '0'
                    else:
                        b -= 2
                        s[i] = s[-(i + 1)] = '1'
            if '?' in s or a<0 or b<0:
                print(-1)
            else:
                print(''.join(s))