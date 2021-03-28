

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    thing=0
    last=s[0]
    thing=0
    for i in s[1:]:
        if i!=last and last=="1":
            thing+=1
        last=i
        
    left=0
    if s[0]=="0":
        for i in range(n):
            if s[i]=="1":
                break
            left+=1
            
    right=0
    if s[-1]=="1":
        for i in range(n-1, -1, -1):
            if s[i]=='0':
                break
            right+=1
            
    ans=''
    if thing>0:
        ans = left*'0' + '0' + right*'1'
    else:
        ans = left*'0' + right*'1'
    print(ans)
        
        
        
        
    
