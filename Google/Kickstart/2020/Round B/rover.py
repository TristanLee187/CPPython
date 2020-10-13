def simplify (x):
    mult = [1]
    ans = ''
    for i in x:
        if i >= '1' and i <= '9':
            C = int(i)
            mult += [mult[-1]*C]
        elif i == ')':
            mult = mult[:len(mult)-1]
        elif i > '9':
            ans += str(mult[-1]*i)
    return ans
        
            
tests = int(input())
count = 0
while count<tests:
    ns = 1
    ew = 1
    i = input()
    i = simplify(i)
    for j in i:
        if j=='N':
            ns -= 1
            if ns==0:
                ns = 10**9
        elif j=='S':
            ns += 1
            if ns==10**9+1:
                ns = 1
        elif j=='W':
            ew -= 1
            if ew==0:
                ew=10**9
        else:
            ew += 1
            if ew==10**9+1:
                ew=1

    print('Case #' + str(count + 1) + ': ' + str(ew) + ' ' + str(ns))
    count += 1



    
