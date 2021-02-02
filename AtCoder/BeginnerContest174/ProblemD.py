n=int(input())
s=input()
ids=[]
ams=[]
last=s[0]
acc=0
for i in s:
    if i==last:
        acc+=1
    else:
        ids.append(last)
        ams.append(acc)
        acc=1
    last=i

ids.append(last)
ams.append(acc)

print(ids)
print(ams)

    

        
