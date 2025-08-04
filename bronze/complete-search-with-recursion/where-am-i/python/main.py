from collections import defaultdict

with open("whereami.in","r") as fin:
    N = int(fin.readline().strip())
    houses = fin.readline().strip()

def solve():
    count = defaultdict(int)
    for length in range(1,N+1):
        seen = {houses[i:i+length] for i in range(N - length + 1)}
        if len(seen) == N - length + 1:
            return length
    return N

with open("whereami.out","w") as fout:
    print(solve(),file=fout)