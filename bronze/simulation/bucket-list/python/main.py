
# https://usaco.org/index.php?page=viewproblem2&cpid=856

with open("blist.in","r") as read:
    n = int(read.readline())
    cows = [list(map(int,read.readline().split())) for _ in range(n)]

max_time = max(t for _, t, _ in cows)

time = [0] * (max_time+1)

for s, t, b in cows:
    for i in range(s, t+1):
        time[i] += b

with open("blist.out","w") as out:
    print(max(time),file=out)

    
