prob="leapfrog_ch_2_input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=''
#
#Read input
for _ in range(rn()):
    s=rs()
    a = len(s) - 1
    b = s.count('B')
    add='Y' if (a==2 and b==1) or a>b>=2 else 'N'
    ans+='Case #{}: {}\n'.format(_+1,add)
#
file.close()


file=open(prob+".out","w")
file.write(str(ans))
file.close()
