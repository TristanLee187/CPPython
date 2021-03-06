rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

from bisect import bisect_left

def isvalid(i,j,k,l,h,m):
    ans=(10*int(i)+int(j))<h and (10*int(k)+int(l))<m
    def reverse(char):
        if char in [1,0,8]:
            return char
        if char==2:
            return 5
        return 2
    rev=[reverse(c) for c in [l,k,j,i]]
    ans = ans and (10 * int(rev[0]) + int(rev[1])) < h and (10 * int(rev[2]) + int(rev[3])) < m
    return ans
for _ in range(rn()):
    h,m=rns()
    s=rs()
    good=[0,1,2,5,8]
    times=[]
    for i in good:
        for j in good:
            for k in good:
                for l in good:
                    if isvalid(i,j,k,l,h,m):
                        time=str(i)+str(j)+':'+str(k)+str(l)
                        ttime=(10*int(i)+int(j))*m + (10*int(k)+int(l))
                        times.append([ttime,time])
    times.sort()
    atimes=[i[0] for i in times]
    find=(10*int(s[0])+int(s[1]))*m + (10*int(s[3])+int(s[4]))
    i=bisect_left(atimes,find)%len(atimes)
    ans=times[i][1]
    print(ans)