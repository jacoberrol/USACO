with open("cowtip.in","r") as fin:
    N = int(fin.readline().strip())
    grid = [[int(c) for c in fin.readline().strip()] for _ in range(N)]

parity = [
    [0 for _ in range(N)] 
    for _ in range(N)
]

toggle_count = [0]

def is_flipped(cell):
    row, col = cell
    return (grid[row][col] ^ parity[row][col])

def toggle(cell):
    row, col = cell
    for r in range(row+1):
        for c in range(col+1):
            parity[r][c] ^= 1

    toggle_count[0] += 1

candidates = [
    (row,col) 
    for col in range(N-1,-1,-1) 
    for row in range(N-1,-1,-1)]

for cell in candidates:
    if is_flipped(cell): toggle(cell)

with open("cowtip.out","w") as fout:
    print(toggle_count[0],file=fout)