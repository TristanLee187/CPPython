for _ in range(int(input())):
    n=int(input())
    def solve(n):
        ans=[]
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                ans.append(i)
                n/=i
                break
        if len(ans)==0:
            return []
        for i in range(2,int(n**0.5)+1):
            if n%i==0 and i!=ans[0] and n/i!=ans[0] and i!=n/i:
                ans.append(i)
                ans.append(int(n/i))
                break
        return ans
    ans=solve(n)
    if len(ans)!=3:
        print('NO')
    else:
        print('YES')
        print(' '.join(list(map(str,ans))))

