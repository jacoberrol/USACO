from collections import defaultdict

with open("citystate.in","r") as fin:
    N = int(fin.readline().strip())
    cities = [(city[0:2], state) for city, state in (fin.readline().split() for _ in range(N))]

count = defaultdict(int)
for city, state in cities:
    if city != state:
        count[(city,state)] += 1

ans = 0
for (city,state), freq in count.items():
    if (state,city) in count:
        ans += freq * count[(state,city)]

with open("citystate.out","w") as fout:
     print(ans//2,file=fout)