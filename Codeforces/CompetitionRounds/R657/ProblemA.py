def good(s):
    for i in range(len(s)):
        if s[i]!="abacaba"[i] and s[i]!='?':
            return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    
    ians=[]
    ans=False
    acc=[]
    
    for i in range(n-6):
        if i not in acc:
            if good(s[i:i+7]):
                tans=True
                for j in range(i+1,n-6):
                    if s[j:j+7]=='abacaba':
                        if '?' not in s[i:i+7]:
                            acc.append(j)
                        tans=False
                        break
                if tans:
                    ians=[i,i+7]
                    ans=True
                    break
    
    if ans:
        print('yes')
        p=s[:ians[0]]
        p=p.replace('?','z')
        s=s[ians[1]:]
        s=s.replace('?','z')
        print(p+'abacaba'+s)
    else:
        print('no')
            
        

