n,q=map(int,input().split())
s=input()
le=len
mi=min
ra=range
def eval(string):
    ans=(le(string)+1)*[0]
    l={}
    stack=[]
    for j in ra(1,le(string)+1):
        i=j-1
        if string[i] not in l:
            l[string[i]]=[i,string[i]]
            ans[j]=(ans[j-1]+1)
            for char in stack:
                l[char][1]=mi(l[char][1],string[i])
            stack.append(string[i])
        else:
            if l[string[i]][1]<string[i]:
                ans[j]=(ans[j-1]+1)
                l[string[i]][1]=string[i]
            else:
                ans[j]=(ans[j-1])
                l[string[i]][1]=string[i]
            for char in stack:
                l[char][1]=mi(l[char][1],string[i])
    return ans

pres=eval(s)
suff=eval(s[::-1])
for i in ra(q):
    l,r=map(int,input().split())
    print(pres[l-1]+suff[n-r])