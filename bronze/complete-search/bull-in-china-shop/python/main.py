import sys
from pprint import pprint

def read_shape(grid):
    return {
        (r, c)
        for r, row in enumerate(grid)
        for c, ch in enumerate(row) 
        if ch == '#'
    }

def valid_shifts(shape, N):
    min_r = min(r for r, _ in shape)
    max_r = max(r for r, _ in shape)
    min_c = min(c for _, c in shape)
    max_c = max(c for _, c in shape)

    return [
        (dr, dc)
        for dr in range(-min_r,    N - max_r)
        for dc in range(-min_c,    N - max_c)
    ]

def shift(shape, dr, dc):
    return {(r + dr, c + dc) for r, c in shape}

with open("bcs.in","r") as fin, open("bcs.out","w") as fout:
   N, K = map(int,fin.readline().split())
   figurine_grid = [list([c for c in fin.readline().strip()]) for _ in range(N)]
   pieces_grids = [
      [list([c for c in fin.readline().strip()]) for _ in range(N)]
      for _ in range(K)
   ]

   figurine = read_shape(figurine_grid)
   pieces   = [read_shape(g) for g in pieces_grids]
   shifts   = [valid_shifts(p, N) for p in pieces]

   for i in range(K):
      for j in range(i + 1, K):
         for dr1, dc1 in shifts[i]:
               s1 = shift(pieces[i], dr1, dc1)
               for dr2, dc2 in shifts[j]:
                  s2 = shift(pieces[j], dr2, dc2)
                  if (s1 | s2) == figurine:
                     print(f"{i+1} {j+1}",file=fout)
                     sys.exit(0)
