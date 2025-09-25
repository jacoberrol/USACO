import itertools

with open("div7.in","r") as fin:
    N = int(fin.readline().strip())

    first, last = [None]*7, [None]*7

    s = 0
    first[0] = last[0] = 0
    for i in range(N):
        s = (s + int(fin.readline().strip())) % 7
        if first[s] is None:
            first[s] = i
        last[s] = i

    ans = max((last[r] - first[r]) for r in range(7) if first[r] is not None)

with open("div7.out","w") as fout:
    print(ans,file=fout)