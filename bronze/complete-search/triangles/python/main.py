from collections import defaultdict

with open("triangles.in","r") as fin:
    n = int(fin.readline().strip())
    posts = [tuple(map(int,fin.readline().strip().split())) for _ in range(n)]

rows = defaultdict(list)
cols = defaultdict(list)

for x, y in posts:
    rows[y].append((x,y))
    cols[x].append((x,y))

for _, row in rows.items():
    row.sort(key=lambda r: r[0])

for _, col in cols.items():
    col.sort(key=lambda c: c[1])

output = 0

# now we just need to iterate all row, col combos
# and find the largest triangle
for x, y in posts:
    row = rows[y] # all posts in this row
    col = cols[x] # all cols in this row
    # skip if they don't have at least two posts    
    if len(row) > 1 and len(col) > 1:
        xmin, xmax = row[0][0], row[-1][0]
        ymin, ymax = col[0][1], col[-1][1]
        
        # compute area of all possible right triangles 
        # formed at this fence post
        t1 = abs((xmax - x) * (ymax - y))
        t2 = abs((x - xmin) * (ymax - y))
        t3 = abs((xmax - x) * (y - ymin))
        t4 = abs((x - xmin) * (y - ymin))

        output = max(output,t1,t2,t3,t4)

with open("triangles.out","w") as fout:
    print(output,file=fout)