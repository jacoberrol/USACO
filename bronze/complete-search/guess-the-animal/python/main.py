from collections import defaultdict
from itertools import combinations

with open("guess.in","r") as fin:
    n = int(fin.readline().strip())
    animals = defaultdict(set)
    for _ in range(n):
        name, _, *words = fin.readline().split()
        animals[name].update(words)
        
max_intersection = max (
    len(animals[a] & animals[b])
    for a, b in combinations(animals,2)
)

with open("guess.out","w") as fout:
    print(max_intersection+1, file=fout)