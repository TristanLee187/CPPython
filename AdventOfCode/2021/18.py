from math import ceil
file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

n=100
fish=[]
for i in range(n):
    fish.append(rs())
file.close()

def process(line):
    arr=list(line)
    done=False
    while not done:
        done=True
        depth = -1
        new=[]
        i=0
        while i<len(arr):
            if type(arr[i])==int or arr[i]==',' or arr[i].isnumeric():
                new.append(arr[i])

            elif arr[i]=='[':
                depth+=1
                new.append('[')

            elif arr[i]==']':
                depth-=1
                new.append(']')
                if depth>=3:

                    done=False
                    s=''
                    k=-1
                    while new[k]!='[':
                        s=str(new[k])+s
                        k-=1
                    s='['+s
                    a,b=eval(s)
                    x = len(eval(s))
                    # print('hi',''.join(map(str,new)), s)
                    for j in range(2*x+1):
                        new.pop()
                    for j in range(-1,-len(new)-1,-1):
                        if type(new[j])==int:
                            new[j]+=a
                            break
                        if new[j].isnumeric():
                            new[j] = int(new[j]) + a
                            break
                    for j in range(i, len(arr)):
                        if type(arr[j])==int:
                            arr[j]+=b
                            break
                        if arr[j].isnumeric():
                            arr[j]=int(arr[j])+b
                            break


                    new.append('0')
                    # print(''.join(map(str, arr)))
            i+=1

        new2=[]
        i=0
        while i<len(new):
            if type(new[i])==int and new[i]>9:
                done=False
                aa=new[i]//2
                bb=ceil(new[i]/2)
                new2+=['[',aa,',',bb,']']
                new2+=new[i+1:]
                break
            else:
                new2.append(new[i])
            i+=1
        arr=new2
        # print(''.join(map(str, arr)))

    return ''.join(map(str, arr))


def add(a,b):
    return '['+a+','+b+']'

ans=0
for i in range(n):
    for j in range(i+1,n):
        line=process(add(fish[i],fish[j]))
        pans=0
        factor=1
        for ch in line:
            if ch == '[':
                factor *= 3
            elif ch == ']':
                factor /= 2
            elif ch == ',':
                factor /= 3
                factor *= 2
            elif type(ch) == int:
                pans += factor * ch
            else:
                pans += int(ch) * factor
        ans=max(ans,pans)

print(ans)
