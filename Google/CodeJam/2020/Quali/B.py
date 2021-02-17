for _ in range(int(input())):
    s=input()
    ans=''
    for i in range(len(s)):
        if i==0:
            ans+=int(s[0])*'(' + s[0]
        else:
            diff=int(s[i])-int(s[i-1])
            if diff>=0:
                ans+=diff*'('+s[i]
            else:
                ans+=abs(diff)*')'+s[i]
        if i==len(s)-1:
            ans+=int(s[-1])*')'
    


    print('Case #' + str(_ + 1) + ': ' + ans)