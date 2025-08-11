import math

INF = math.inf

with open("outofplace.in","r") as fin:
    N = int(fin.readline().strip())
    line = [int(fin.readline()) for _ in range(N)]

ans = 0
for i in range(0,N-1):
    curr = line[i]
    prev = line[i-1] if i > 0 else -1
    next = line[i+1] if i < N-1 else INF
    next_next = line[i+2] if i < N-2 else INF
    if curr > next:
        ans = 1
        if next <= prev:
            ans = len({
                c for j, c in enumerate(line) 
                if j < i+1 and next < c
            })
        elif curr >= next_next:
            ans = len({
                c for j, c in enumerate(line) 
                if j > i and curr > c
            })
        break

with open("outofplace.out","w") as fout:
    print(ans,file=fout)