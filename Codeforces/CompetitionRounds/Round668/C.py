for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    def solve(n,k,s):
        l=list(s)
        for i in range(k):
            t=s[i]
            for j in range(i,n,k):
                if s[j]!='?':
                    if t!='?' and s[j]!=t:
                        return False
                    t=s[j]
            for j in range(i,n,k):
                l[j]=t
        return max(l[:k].count('1'),l[:k].count('0')) <= k//2
    if solve(n,k,s):
        print('YES')
    else:
        print('NO')

