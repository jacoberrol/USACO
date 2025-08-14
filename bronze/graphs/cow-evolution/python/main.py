from collections import defaultdict
from itertools import combinations

with open("evolution.in","r") as fin:
    N = int(fin.readline().strip())
    graph = defaultdict(set)
    for pop_id in range(N):
        k, *traits = fin.readline().split()
        for t in traits:
            graph[t].add(pop_id)

def is_proper(traits):
    for A, B in combinations(traits,2):
        if A & B and not (B <= A or A <= B):
            return False
    return True

ans = "yes" if is_proper(sorted(graph.values(),key=len)) else "no"

with open("evolution.out","w") as fout:
    print(ans,file=fout)