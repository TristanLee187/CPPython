file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


class monke:
    def __init__(self, items, op, test, t_monke, f_monke):
        self.items=items
        self.op=op
        self.test=test
        self.t_monke=t_monke
        self.f_monke=f_monke


# part 1
def part_1():
    curr=[]
    monkes=[]
    for line in lines:
        if line:
            # print(line)
            curr.append(line)
        else:
            items = list(map(int,[num.split(',')[0] for num in curr[1].split()[2:]]))
            op = curr[2].split()[4:6]
            if op[1]=='old':
                op = ['**',2]
            test = int(curr[3].split()[-1])
            t_m = int(curr[4].split()[-1])
            f_m = int(curr[5].split()[-1])
            monkes.append(monke(items,op,test,t_m,f_m))
            # print(items,op,test,t_m,f_m)
            curr.clear()
    counts = [0 for i in range(len(monkes))]
    for i in range(20):
        for j in range(len(monkes)):
            m=monkes[j]
            num_items = len(m.items)
            for k in range(num_items):
                counts[j]+=1
                num = m.items.pop(0)
                nnum=eval('{}{}{}'.format(num,m.op[0],m.op[1]))//3
                if nnum%m.test==0:
                    monkes[m.t_monke].items.append(nnum)
                else:
                    monkes[m.f_monke].items.append(nnum)
    counts.sort(reverse=True)
    ans=counts[0]*counts[1]
    return ans


# part 2
def part_2():
    curr=[]
    monkes=[]
    mod=1
    for line in lines:
        if line:
            curr.append(line)
        else:
            items = list(map(int,[num.split(',')[0] for num in curr[1].split()[2:]]))
            op = curr[2].split()[4:6]
            if op[1]=='old':
                op = ['**',2]
            test = int(curr[3].split()[-1])
            t_m = int(curr[4].split()[-1])
            f_m = int(curr[5].split()[-1])
            mod*=test
            monkes.append(monke(items,op,test,t_m,f_m))
            curr.clear()
    counts = [0 for i in range(len(monkes))]
    for i in range(10000):
        for j in range(len(monkes)):
            m=monkes[j]
            num_items = len(m.items)
            for k in range(num_items):
                counts[j]+=1
                num = m.items.pop(0)
                nnum=eval('{}{}{}'.format(num,m.op[0],m.op[1]))
                if nnum%m.test==0:
                    monkes[m.t_monke].items.append(nnum%mod)
                else:
                    monkes[m.f_monke].items.append(nnum%mod)
                # print(i, j, k, nnum)
    counts.sort(reverse=True)
    ans=counts[0]*counts[1]
    return ans


if __name__ == '__main__':
    print(part_1())
    print(part_2())
