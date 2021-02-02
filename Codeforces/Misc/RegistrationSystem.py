d={}
n=int(input())
for i in range(n):
    name=input()
    if name in d:
        print(name + str(d[name]))
        d[name]+=1
    else:
        d[name]=1
        print('OK')
    
