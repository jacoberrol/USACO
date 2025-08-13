with open("swap.in","r") as fin:
    N, K = map(int,fin.readline().split())
    A1, A2 = map(int,fin.readline().split())
    B1, B2 = map(int,fin.readline().split())

swap = list(range(N+1))
swap[A1:A2+1] = swap[A1:A2+1][::-1]
swap[B1:B2+1] = swap[B1:B2+1][::-1]

ans = [0] * (N+1)
visited = [0] * (N+1)

for start in range(1,N+1):
    if not visited[start]:
        path = []
        x = start
        while not visited[x]:
            path.append(x)
            visited[x] = 1
            x = swap[x]
        L = len(path)
        for i, posi in enumerate(path):
            ans[posi] = path[(i + K) % L]

with open("swap.out","w") as fout:
    for i in range(1,N+1):
        print(ans[i],file=fout)
