t=int(input())
count=0
while count<t:
    count+=1
    trash = int(input())
    l = list(map(int, input().split(' ')))
    limit= sum(l)
    alice = l[0]
    bob = 0
    alicemove = l[0]
    bobmove = 0
    moves = 1
    leftright = False
    aindex = 1
    bindex = trash-1
    while alice+bob<limit:
        moves+=1
        if leftright:
            while alicemove<=bobmove and aindex<bindex+1:
                alicemove += l[aindex]
                aindex+=1
            bobmove = 0
            alice += alicemove
            leftright = False
        else:
            while bobmove<=alicemove and bindex+1>aindex:
                bobmove += l[bindex]
                bindex -= 1
            alicemove = 0
            bob += bobmove
            leftright = True

    print(moves, alice, bob)
        
