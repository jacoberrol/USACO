N = int(input().strip())
grid = [list(map(int,input().split())) for _ in range(N)]

row_total = 0
for r in range(N):
    even_sum = sum(grid[r][c] for c in range(0, N, 2))
    odd_sum  = sum(grid[r][c] for c in range(1, N, 2))
    row_total += max(even_sum, odd_sum)

col_total = 0
for c in range(N):
    even_sum = sum(grid[r][c] for r in range(0, N, 2))
    odd_sum  = sum(grid[r][c] for r in range(1, N, 2))
    col_total += max(even_sum, odd_sum)

print(max(row_total,col_total))