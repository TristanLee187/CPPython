from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    def solve():
        n,diff=rns()
        a=rl()
        if diff==1:
            return True
        b=sorted(a)
        if a==b:
            return True
        if diff==n:
            return False
        diffs = [i for i in range(n) if a[i]!=b[i]]
        diffs = [max(i,n-1-i) for i in diffs]
        # print(diffs)
        return min(diffs)>=diff

    YN(solve())
