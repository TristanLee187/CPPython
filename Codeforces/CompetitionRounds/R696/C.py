rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    l.sort()
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    if n==1:
        YN(True)
    else:
        ans=True
        if l[-1]-l[-2] not in d and l[-1]-l[-3] not in d:
            ans=False
        def dfs(a,dict,test,solution,lr):
            from bisect import bisect_left
            if len(dict)==1 and lr or len(dict)==0:
                return solution
            test1=a[bisect_left(a,test)-1]
            b = dict.copy()
            bchange=False
            solution2=solution.copy()
            if test-test1 in dict and dict[test-test1]>0:
                bchange=True
                b[test]-=1
                if b[test]==0:
                    b.__delitem__(test)
                b[test1]-=1
                if b[test1]==0:
                    b.__delitem__(test1)
                if test-test1 not in b:
                    bchange=False
                else:
                    b[test-test1]-=1
                    if b[test-test1]==0:
                        b.__delitem__(test-test1)
                solution2.append([test1,test-test1])
            if lr==False:
                if len(b)==len(dict):
                    return False
                else:
                    return dfs(a,b,test1,solution2,lr)
            else:
                if len(b)==1:
                    return solution2
                c=dict.copy()
                cchange=False
                solution3 = solution.copy()
                test2 = a[bisect_left(a, test) - 2]
                if test - test2 in dict and dict[test - test2] > 0:
                    cchange=True
                    c[test] -= 1
                    if c[test] == 0:
                        c.__delitem__(test)
                    c[test2] -= 1
                    if c[test2] == 0:
                        c.__delitem__(test2)
                    if test-test2 not in c:
                        cchange=False
                    else:
                        c[test - test2] -= 1
                        if c[test - test2] == 0:
                            c.__delitem__(test - test2)
                    solution3.append([test2, test - test2])
                if not bchange and cchange:
                    return dfs(a,c,test2,solution3,lr=False)
                if bchange and not cchange:
                    return dfs(a, b, test1,solution2, lr=True)
                if bchange and cchange:
                    return dfs(a, b, test1, solution2, lr=True) or dfs(a,c,test2,solution3,lr=False)
                else:
                    return False
        m=l[-1]
        sol=[]
        tans=dfs(l,d,m,sol,lr=True)
        if tans==False:
            YN(False)
        else:
            for i in tans:
                d[i[0]]-=1
                d[i[1]]-=1
            extra=[]
            for i in d:
                if d[i]>0:
                    extra+=[i]
            tans=[extra]+tans
            pans=sum(extra)
            if tans and ans:
                YN(True)
                print(pans)
                for i in tans:
                    print(*i)
            else:
                YN(False)
