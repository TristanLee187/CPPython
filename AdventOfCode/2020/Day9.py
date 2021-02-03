a=[]
for i in range(1000):
    a.append(int(input()))

# for i in range(25,1000):
#     b=[]
#     for j in range(i-25,i):
#         for k in range(i-25,i):
#             if j!=k:
#                 b.append(a[j]+a[k])
#     if a[i] not in b:
#         print(a[i])
#         break


find=731031916
for i in range(1000):
    minimum=float('inf')
    maximum=0
    pos=0
    for j in range(i+1,1000):
        pos+=a[j]
        minimum=min(minimum,a[j])
        maximum=max(maximum,a[j])
        if pos==find:
            print(minimum+maximum)
            break