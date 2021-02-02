tests = int(input())
count = 0
while count<tests:
    mounts = int(input())
    hills = input()
    thills = hills.split(' ')
    peaks = 0
    for i in list(range(1,len(thills)-1)):
        if int(thills[i])>int(thills[i-1]) and int(thills[i])>int(thills[i+1]):
            peaks += 1
    print('Case #:' + str(count + 1) + ': ' + str(peaks))
    count+=1


    
