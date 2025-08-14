with open("family.in","r") as fin:
    N, A, B = fin.readline().split()
    N = int(N)
    graph = {b: a for a, b in (fin.readline().split() for _ in range(N))}
    
def get_ancestors(name,graph):
    x = name
    ancestors = [x]
    while x in graph:
        x = graph[x]
        ancestors.append(x)
    return ancestors

def get_nearest_ancestor(anc_A,anc_B):
    for ia, a in enumerate(anc_A):
        for ib, b in enumerate(anc_B):
            if a==b:
                return (ia,ib)
    return None

def get_relationship(dist_A,dist_B):

    x, y, dx, dy = (A, B, dist_A, dist_B) if dist_A < dist_B else (B, A, dist_B,dist_A)
    if dx == 1 and dy == 1:
        return "SIBLINGS"
    if dx == 0 and dy == 1:
        return f"{x} is the mother of {y}"
    if dx == 0 and dy == 2:
        return f"{x} is the grand-mother of {y}"
    if dx == 0 and dy > 2:
        return f"{x} is the {'great-'*(dy-2)}grand-mother of {y}"
    if dx == 1 and dy == 2:
        return f"{x} is the aunt of {y}"
    if dx == 1 and dy > 2:
        return f"{x} is the {'great-'*(dy-2)}aunt of {y}"

    return "COUSINS"

anc_A = get_ancestors(A,graph)
anc_B = get_ancestors(B,graph)

common_ancestor = get_nearest_ancestor(anc_A,anc_B)

ans = "NOT RELATED"
if common_ancestor:
    ans = get_relationship(common_ancestor[0],common_ancestor[1])

with open("family.out","w") as fout:
    print(ans,file=fout)

