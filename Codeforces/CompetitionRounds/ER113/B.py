from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    if 0<s.count('2')<3:
        print('NO')
    else:
        print('YES')
        ans=[n*[' '] for i in range(n)]
        for i in range(n):
            ans[i][i]='X'
        twos=[]
        for i in range(n):
            if s[i]=='1':
                for j in range(n):
                    if i!=j:
                        ans[i][j]='='
                        ans[j][i]='='
            else:
                twos.append(i)
        for i in range(len(twos)-1):
            ans[twos[i]][twos[i+1]]='+'
            ans[twos[i+1]][twos[i]] = '-'
        if len(twos):
            ans[twos[-1]][twos[0]]='+'
            ans[twos[0]][twos[-1]] = '-'
        for i in range(n):
            for j in range(n):
                if ans[i][j]==' ':
                    ans[i][j]='='
        for row in ans:
            print(''.join(row))


