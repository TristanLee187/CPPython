t=int(input())
count=0
while count<t:
    count+=1
    n = int(input())
    s = input()
    s = s.split(' ')
    m = int(s[0])
    prev = int(s[0])
    Sum=0
    for i in s[1:]:
        if 1.0*int(i)/prev<0:
            Sum += m
            prev = int(i)
            m = int(i)
        else:
            m = max(m,int(i))
            prev = int(i)
    Sum+=m
    print(Sum)
