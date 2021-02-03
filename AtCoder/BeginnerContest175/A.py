s=input()
if s=='RRR':
    print(3)
elif s[:2]=='RR' or s[1:]=='RR':
    print(2)
elif 'R' in s:
    print(1)
else:
    print(0)