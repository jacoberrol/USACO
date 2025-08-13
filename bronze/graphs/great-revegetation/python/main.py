from functools import reduce
from operator import or_

SEEDS = (1,2,3,4)

with open("revegetate.in","r") as fin:
    N, M = map(int,fin.readline().split())
    adjacent = [set() for _ in range(N+1) ]
    for _ in range(M):
        a, b = map(int,fin.readline().split())
        adjacent[a].add(b)
        adjacent[b].add(a)

planted = [0] * (N+1)

for pasture in range(1,N+1):
    used = reduce(or_, (1 << planted[p] for p in adjacent[pasture]), 0)
    planted[pasture] = next(s for s in SEEDS if not (used & (1 << s)))

with open("revegetate.out","w") as fout:
    print("".join(map(str,planted[1:])),file=fout)