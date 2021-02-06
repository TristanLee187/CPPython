l=1
r=1000000
while l!=r:
    mid=(l+r+1)//2
    print(mid)
    s=input()
    if s=='<':
        r=mid-1
    else:
        l=mid
print('!',l)