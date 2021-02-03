rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(int(input())):
    l,r=input().split()
    def good(n):
        for i in range(len(str(n))):
            if int(not(i%2))!=int(str(n)[i])%2:
                return False
        return True
    ans=0
    if good(l):
        ans+=1
    l=list(map(int,list(l)))
    r=list(map(int,list(r)))
    def solve(s):
        num=[]
        i=0
        while i<len(s):
            if s[i]%2==int(not(i%2)):
                num+=[int(s[i])]
                i+=1
            else:
                if s[i]==0:
                    num.append(0)
                    while i>0 and num[i]<2:
                        num[i]=8+int(not(i%2))
                        i-=1
                    num[i]-=2

                else:
                    num+=[s[i]-1]
                break
        while len(num)<len(s):
            num.append(8+int(not(len(num)%2)))
        if num[0]==-1:
            num.pop(0)
            for i in range(len(num)):
                num[i]=8+int(not(i%2))
        ans=1
        for i in range(len(num)):
            a=num[len(num)-i-1]
            ans+=(a//2)*5**i
        for i in range(1,len(num)):
            ans+=5**i
        return ans
    ans+=solve(r)-solve(l)
    print('Case #' + str(_ + 1) + ': ' + str(ans))
