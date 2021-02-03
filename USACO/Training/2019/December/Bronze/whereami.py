file = open("whereami.in")
n=int(file.readline())
s=file.readline()
file.close()

d={}
for i in range(n):
    for j in range(i,n+1):
        word=s[i:j]
        if word in d:
            d[word]+=1
        else:
            d[word]=1
ans=1
for i in d:
    if d[i]>1:
        ans=max(ans,len(i)+1)

file = open("whereami.out", "w")
file.write(str(ans))
file.close()