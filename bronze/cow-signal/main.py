# cow signal solution
# https://usaco.org/index.php?page=viewproblem2&cpid=665

with open("cowsignal.in","r") as read:
    m, n, k = map(int,read.readline().split())
    lines = [read.readline().strip() for _ in range(m)]

with open("cowsignal.out","w") as out:
    for line in lines:
        signal = ''.join([c * k for c in line])
                
        for _ in range(k):
            print(signal,file=out)
        

