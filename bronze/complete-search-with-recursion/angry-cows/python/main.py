import bisect
from collections import deque

with open("angry.in","r") as fin:
    N = int(fin.readline().strip())
    bales = {int(fin.readline().strip()) for _ in range(N)}

bales_list = sorted(bales)

def solve(start):

    q = deque()
    q.append((start,1))
    hits = set()

    while q:
        pos, radius = q.popleft()
        # confirm this is a valid hit
        if pos not in hits:
            hits.add(pos)
            
            # enqueue next hits
            lo = bisect.bisect_left(bales_list, pos - radius)
            hi = bisect.bisect_right(bales_list, pos + radius)
            for i in range(lo,hi):
                neighbor = bales_list[i]
                if neighbor not in hits:
                        q.append((neighbor,radius+1))

    return len(hits)

max_hits = 0
for i in bales:
    max_hits = max(solve(i), max_hits)

with open("angry.out","w") as fout:
    print(max_hits,file=fout)