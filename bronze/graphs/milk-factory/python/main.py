with open("factory.in","r") as fin:
    N = int(fin.readline().strip())
    outdeg = [0] * (N+1)
    for _ in range(N-1):
        a, _ = map(int,fin.readline().split())
        outdeg[a] += 1

ans = [i for i, outs in enumerate(outdeg[1:],1) if outs == 0]

with open("factory.out","w") as fout:
    print(ans[0] if len(ans) == 1 else -1, file=fout)