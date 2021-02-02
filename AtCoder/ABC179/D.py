n,k=map(int,input().split())
l=[]
for i in range(k):
    l.append(list(map(int,input().split())))
l.sort()
dp=n*[0]
