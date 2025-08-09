from collections import Counter

with open("hoofball.in","r") as fin:
    N = int(fin.readline().strip())
    cows = sorted([int(c) for c in fin.readline().split()])

nearest = lambda i: (
    1 if i == 0 else
    N - 2 if i == N - 1 else
    i - 1 if cows[i] - cows[i - 1] <= cows[i + 1] - cows[i] else i + 1
)

pass_to = [nearest(i) for i in range(N)]

inbound = Counter(pass_to)

zero_inbound = sum(1 for i in range(N) if inbound[i] == 0)

is_pair = lambda i: (
    pass_to[i] == i + 1
    and pass_to[i + 1] == i
    and inbound[i] == 1
    and inbound[i + 1] == 1
)

isolated_pairs = sum(is_pair(i) for i in range(N - 1))

with open("hoofball.out","w") as fout:
    print(zero_inbound+isolated_pairs,file=fout)