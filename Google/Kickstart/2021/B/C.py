from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)

def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for _ in range(rn()):
    z=rn()
    root=int(z**0.5)
    test=root
    nums=[]
    while len(nums)<2:
        if isPrime(test):
            nums.append(test)
        test-=1
    test=root+1
    while len(nums)==2:
        if isPrime(test):
            nums.append(test)
        test+=1
    nums.sort()
    ans=nums[0]*nums[1]
    if nums[1]*nums[2]<=z:
        ans=nums[1]*nums[2]

    print('Case #' + str(_+1)+': ' + str(ans))