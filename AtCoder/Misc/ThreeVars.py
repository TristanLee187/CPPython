i = input().split(' ')
A = int(i[1])
B = int(i[2])
C = int(i[3])
ans = ''
count=0
while count<int(i[0]):
    move = input()
    if move=='AB':
        up = min(A,B)
        if A==up:
            ans += 'A' + '\n'
        else:
            ans += 'B' + '\n'
        if up==A:
            A+=1
            B-=1
        else:
            A-=1
            B+=1
    elif move=='AC':
        up = min(A,C)
        if A==up:
            ans += 'A' + '\n'
        else:
            ans += 'C' + '\n'
        if up==A:
            A+=1
            C-=1
        else:
            A-=1
            C+=1
    else:
        up = min(B,C)
        if B==up:
            ans += 'B' + '\n'
        else:
            ans += 'C' + '\n'
        if up==B:
            B+=1
            C-=1
        else:
            B-=1
            C+=1
    count+=1
    m = min(A,B,C)
    if m<0:
        print('No')
        break

m = min(A,B,C)
if m>=0:
    print('Yes')
    print(ans, end='')
