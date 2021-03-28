t = int(input())
for _ in range(t):
    s=input()
    n=int(input())
    def solve(s,n):
        ans=len(s)*[-1]
        for i in range(len(s)-n,n):
            if s[i]==1:
                return '-1'
        for i in range(len(s)):
            if i<n and i+n<len(s):
                ans[i+n]=s[i]
            elif len(s)-i<=n:
                if i-n>=0 and ans[i-n]!=-1 and ans[i-n]!=s[i]:
                    return '-1'
                if i-n>=0 and ans[i-n]==-1:
                    ans[i-n]=s[i]
        for i in range(len(s)):
            if i>=n and len(s)-i>n:
                if s[i]=='1':
                    if ans[i-n]==-1:
                        ans[i-n]=s[i]
                    elif ans[i+n]==-1:
                        ans[i+n]=s[i]
                    elif ans[i-n]==ans[i+n]==0:
                        return '-1'
                else:
                    if ans[i-n]=='1' or ans[i+n]=='1':
                        return '-1'
                    else:
                        ans[i - n] = s[i]
                        ans[i + n] = s[i]

        for i in range(len(s)):
            if ans[i]==-1:
                ans[i]=1

        return ''.join(list(map(str,ans)))

    print(solve(s,n))





