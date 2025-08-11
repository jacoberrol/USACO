import math

def int_sqrt(n):
    return int(math.sqrt(n))

def time_for(K, x):
    root = int_sqrt(K)
    if root * root < K:
        root += 1
    p = max(x, root)
    r = p*p - K
    m = (int_sqrt(8*r + 1) - 1) // 2
    return (2*p - 1) - m

with open("race.in") as fin:
    K, N = map(int, fin.readline().split())
    X = [int(fin.readline()) for _ in range(N)]

with open("race.out", "w") as fout:
    for x in X:
        print(time_for(K, x), file=fout)
