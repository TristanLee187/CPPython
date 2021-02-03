"""
ID: tristan16
LANG: PYTHON3
PROB: beads
"""

a=open('beads.in', 'r')
b=open('beads.out', 'w')

n=int(a.readline())
s=a.read().strip()

def amount(string):
    right=0
    i=0
    acc=[]
    while i<len(string):
        if string[i] in acc:
            right+=1
            i+=1
        elif string[i]=='w':
            right+=1
            i+=1
            acc.append('w')
        else:
            a=len(acc)
            if 'w' in acc:
                a-=1
            if a==1:
                break
            else:
                right+=1
                acc.append(string[i])
                i+=1
    left=0
    i=len(string)-1
    acc=[]
    while i>=right:
        if string[i] in acc:
            left+=1
            i-=1
        elif string[i]=='w':
            left+=1
            i-=1
            acc.append('w')
        else:
            a=len(acc)
            if 'w' in acc:
                a-=1
            if a==1:
                break
            else:
                left+=1
                acc.append(string[i])
                i-=1
    return right+left
        


ans=amount(s)
for i in range(1,n):
    s=s[1:]+s[0]
    ans = max(ans,amount(s))

b.write(str(ans)+'\n')
a.close()
b.close()

    
    
    
