N, Q = map(int,input().split())
forest = [[1 if x=='*' else 0 for x in input()] for _ in range(N)]
queries = [[int(x) for x in input().split()] for _ in range(Q)]

psum = [[0] * (N+1) for _ in range(N+1)]

for row in range(N):
    for col in range(N):
        psum[row+1][col+1] += (
            psum[row][col+1] + psum[row+1][col] - psum[row][col] + forest[row][col]
        )

for y1, x1, y2, x2 in queries:
    tl, tr, bl, br = psum[y1-1][x1-1], psum[y1-1][x2], psum[y2][x1-1], psum[y2][x2]
    print(br - tr - bl - tl)