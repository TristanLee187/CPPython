for _ in range(int(input())):
    s=input()
    if len(set(s))==1:
        print(s)
    else:
        print(len(s)*'10')