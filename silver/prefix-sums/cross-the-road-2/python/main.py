with open("maxcross.in","r") as fin:
    N, K, B = map(int,fin.readline().split())
    broken = [0]*(N+1)
    for _ in range(B):
        broken[int(fin.readline().strip())] = 1

    for i in range(1,N+1):
        broken[i] += broken[i-1]

print(broken)

ans = K
for r in range(K,N+1):
    ans = min(ans,broken[r] - broken[r-K])

with open("maxcross.out","w") as fout:
    print(ans,file=fout)