t=int(input())
count=0
while count<t:
    count+=1
    n = int(input())
    l = list(map(int, input().split(' ')))
    l = sorted(l)
    index = 0
    index2 = 1
    ans1 = 0
    while index<len(l):
        if max(l[index:index2])<=index2-index+1:
            ans1+=1
            index+=index2
            index2 = index+1
        else:
            index2=max(l[index:index2])
    print(ans1)
    
