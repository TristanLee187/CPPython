rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

from bisect import bisect_right
for _ in range(rn()):
    rans=0
    n,m=rns()
    a=rl()
    b=rl()
    ar=[i for i in a if i>0]
    br=[i for i in b if i>0]
    if len(ar)>0 and len(br)>0:
        s=set(br)
        already=[]
        for i in ar:
            if i in s:
                already.append(i)
        already.reverse()
        rans=len(already)
        i = 0
        curr=bisect_right(ar,br[i])
        if len(already)>0 and br[i]==already[-1]:
            already.pop()
        rans=max(rans,len(already)+min(1,curr))
        j=i+1
        while j<len(br):
            if len(already)>0 and br[j]==already[-1]:
                already.pop()
            if i==j:
                rans=max(rans,min(1,curr))
                j+=1
            elif br[j]-br[i]+1<=curr:
                if len(already) > 0 and br[j] == already[-1]:
                    already.pop()
                rans=max(rans,j-i+1+len(already))
                j+=1
            else:
                i+=1
                if i<len(br):
                    curr = bisect_right(ar, br[i])
    lans=0
    ar=[-i for i in a if i<0][::-1]
    br=[-i for i in b if i<0][::-1]
    if len(ar) > 0 and len(br) > 0:
        s = set(br)
        already = []
        for i in ar:
            if i in s:
                already.append(i)
        already.reverse()
        lans = len(already)
        i = 0
        curr = bisect_right(ar, br[i])
        if len(already) > 0 and br[i] == already[-1]:
            already.pop()
        lans = max(lans, len(already) + min(1, curr))
        j = i + 1
        while j < len(br):
            if len(already) > 0 and br[j] == already[-1]:
                already.pop()
            if i==j:
                lans = max(lans, min(1, curr))
                j+=1
            elif br[j] - br[i] + 1 <= curr:
                lans = max(lans, j - i + 1 + len(already))
                j += 1
            else:
                i += 1
                if i<len(br):
                    curr = bisect_right(ar, br[i])
    print(rans+lans)