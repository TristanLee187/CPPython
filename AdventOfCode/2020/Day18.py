a=[]
def f(s):
    l = []
    for i in s:
        if i != ' ':
            l.append(i)
    i=0
    while i<len(l):
        if l[i]=='+':
            j=i-1
            acc=0
            if l[j]==')':
                acc+=1
            j-=1
            while acc>0 and j>0:
                if l[j]==')':
                    acc+=1
                elif l[j]=='(':
                    acc-=1
                j-=1
            left=j
            j = i + 1
            acc = 0
            if l[j] == '(':
                acc += 1
            j += 1
            while acc > 0 and j < len(l):
                if l[j] == '(':
                    acc += 1
                elif l[j] == ')':
                    acc -= 1
                j += 1
            right = j
            l.insert(left+1,'(')
            l.insert(right+1,')')
            i+=2
        else:
            i+=1
    return l
for i in range(372):
    s=input()
    a.append(f(s))
ans=0
def eval(exp):
    res=0
    a=[]
    acc=0
    for i in exp:
        if i=='(':
            acc+=1
            a.append(acc)
        elif i==')':
            a.append(acc)
            acc-=1
        else:
            a.append(acc)
    a.append(0)
    i=0
    op=''
    while i<len(a)-1:
        if a[i]>0:
            newexp=exp[i+1:a.index(a[i]-1,i+1)-1]
            tres=eval(newexp)
            i=a.index(a[i]-1,i+1)
            if op=='':
                res=tres
            elif op=='*':
                res*=tres
            else:
                res+=tres
        elif exp[i]=='*' or exp[i]=='+':
            op=exp[i]
            i+=1
        else:
            if op=='':
                res=int(exp[i])
            elif op=='*':
                res*=int(exp[i])
            else:
                res+=int(exp[i])
            i+=1
    print(exp,a,res)
    return res
for i in a:
    ans+=eval(i)
print(ans)