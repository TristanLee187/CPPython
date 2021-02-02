t = int(input())
count=0
while count<t:
    count+=1
    n = input()
    ans = 0
    string = ''
    for i in list(range(len(n))):
        if n[i]!='0':
            ans+=1
            string += n[i] + (len(n)-i-1)*'0' + ' '
    print(ans)
    print(string)
            
