rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s=rs()
    if s[0]=='a' and len(set(s))==1:
        print('NO')
    elif 'a'+s != s[::-1]+'a':
        print('YES')
        print('a'+s)
    elif s+'a' != 'a'+s[::-1]:
        print('YES')
        print(s+'a')
    else:
        print('NO')