from collections import defaultdict

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=42
all_ings=[]
allergens_pos=defaultdict(set)
for i in range(n):
    s=rs()
    l,r=s.index('('),s.index(')')
    ings = set(s[:l].split())
    all_ings += ings
    algs = s[l+1:r].split()[1:]
    for j in range(len(algs)):
        if ',' in algs[j]:
            algs[j] = algs[j].replace(',','')
    for alg in algs:
        if len(allergens_pos[alg])==0:
            allergens_pos[alg]=ings.copy()
        else:
            allergens_pos[alg] &= ings

# for alg in allergens_pos:
#     print(alg, allergens_pos[alg])
aller_ings = set()
for alg in allergens_pos:
    for ing in allergens_pos[alg]:
        aller_ings.add(ing)
# print(aller_ings)
for ing in all_ings:
    if ing not in aller_ings:
        ans+=1
file.close()

print(ans)
known = {'shellfill': 'rkzqs', 'sesame':'ctmzsr', 'fish':'hphcb', 'soy':'zmhnj', 'peanuts':'vzzxl', 'eggs':'zjsh',
         'nuts':'mbdksj', 'dairy':'vrzkz'}
for ing in known.values():
    new = {}
    for algg in allergens_pos:
        if ing in allergens_pos[algg]:
            allergens_pos[algg].remove(ing)

ans2=''
for alg in sorted(known.keys()):
    ans2+=known[alg]+','

print(ans2)
