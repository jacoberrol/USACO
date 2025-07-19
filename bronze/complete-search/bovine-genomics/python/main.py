with open("cownomics.in","r") as fin:
    n, m = map(int,fin.readline().split())
    spotty = [fin.readline().strip() for _ in range(n)]
    plain = [fin.readline().strip() for _ in range(n)]

spotty_genes = [set(pos) for pos in zip(*spotty)]
plain_genes = [set(pos) for pos in zip(*plain)]

candidate_count = sum([
    1 
    for spos, ppos in zip(spotty_genes,plain_genes) 
    if spos.isdisjoint(ppos)
])

with open("cownomics.out","w") as fout:
    print(candidate_count,file=fout)