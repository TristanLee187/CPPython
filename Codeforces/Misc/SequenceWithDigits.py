def minDig(x):
    ans = "9"
    for i in x:
        if ans=="1":
            break
        if i<ans:
            ans=i
    return ans

def maxDig(x):
    ans = "0"
    for i in x:
        if ans=="9":
            break
        if i>ans:
            ans=i
    return ans


t = int(input())
count=0
while count<t:
    count+=1
    l = input().split(' ')
    a = l[0]
    k = int(l[1]) - 1
    while k>0:
        k-=1
        a = int(a) + int(minDig(str(a))) * int(maxDig(str(a)))
    print(a)
        
