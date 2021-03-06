rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

from collections import Counter
def solve(n,k,s):
    if n%k!=0:
        return -1
    c=Counter(s)
    if all([c[i]%k==0 for i in c]):
        return True
    d={}
    ans=-1
    for i in range(n):
        for j in range(1,26-(ord(s[i])-97)):
            if ord(s[i])-97+j not in d:
                d[ord(s[i])-97+j]=0
            d[ord(s[i])-97+j]+=1
            a=n-i-1
            flag=False
            for l in d:
                if d[l]>0:
                    if (k-d[l]%k)%k>a:
                        flag=True
                        break
                    a-=(k-d[l]%k)%k
            if not flag and a%k==0:
                ans=[i,j]
                d[ord(s[i]) - 97 + j] -= 1
                break
            else:
                d[ord(s[i]) - 97 + j] -= 1
        if ord(s[i]) - 97 not in d:
            d[ord(s[i]) - 97] = 0
        d[ord(s[i]) - 97] += 1
    return ans
for _ in range(rn()):
    n,k=rns()
    s=rs()
    ans=solve(n,k,s)
    if ans==-1:
        print(-1)
    elif ans==True:
        print(s)
    else:
        pans=''
        for i in range(ans[0]):
            pans+=s[i]
        pans+=chr(ord(s[ans[0]])+ans[1])
        c=Counter(pans)
        d=sorted([[i,c[i]] for i in c])
        tail=''
        for char in d:
            tail+=(k-char[1]%k)%k*char[0]
        fill=n-len(tail)-len(pans)
        print(pans+fill*'a'+tail)