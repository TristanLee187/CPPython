import math

def removeCopies(l):
    i=0
    n=len(l)
    while i<n-1:
        if l[i]==l[i+1]:
            l.pop(i)
            i-=1
            n-=1
        i+=1

n=int(input())
l=list(map(int, input().split(' ')))

l=sorted(l)
removeCopies(l)
if len(l)==1:
    print(0)
else:
    index = 1
    ans=1
    while index<n:
        sindex=0
        tindex=index
        while sindex<tindex:
            if l[index]%l[sindex]==0:
                l.pop(index)
                index-=1
                n-=1
                break
            sindex+=1
        if sindex==tindex:
            ans+=1
        index+=1
    print(ans)
    
