with open("cowqueue.in","r") as fin:
    N = int(fin.readline().strip())
    cows = [tuple(map(int,fin.readline().strip().split())) for _ in range(N)]

cows.sort()

earliest = 0
for arrival, duration in cows:
    earliest = max(earliest,arrival) + duration

with open("cowqueue.out","w") as fout:
    print(earliest,file=fout)