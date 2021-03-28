def prod(l):
    ans=1
    for i in l:
        ans*=i
    return ans
    

n=int(input())
ans=1
while ans**10<n:
    ans+=1
l=10*[ans]
index=0
while prod(l)>n:
    l[index%10]-=1
    index+=1
    
if prod(l)<n:
    l[index%10-1]+=1
string="codeforces"
ans=''
for i in range(10):
    ans += l[i]*string[i]
print(ans)

    
    
    
    
