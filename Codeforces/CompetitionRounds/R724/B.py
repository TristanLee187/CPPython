from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    a=set()
    for i in range(n):
        for j in range(i+1,n+1):
            a.add(s[i:j])
    def inttostr(x):
        if x==0:
            return'a'
        ans=''
        a=x
        while a>=0:
            ans+=chr(a%26+97)
            a=a//26-1
        return ans[::-1]
    ans=0
    while inttostr(ans) in a:
        ans+=1
    print(inttostr(ans))