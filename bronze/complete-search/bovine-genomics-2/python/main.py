from itertools import combinations

with open("cownomics.in","r") as fin:
    n, m = map(int,fin.readline().split())
    spotty = [fin.readline().strip() for _ in range(n)]
    plain = [fin.readline().strip() for _ in range(n)]

spotty_genes = [set(pos) for pos in zip(*spotty)]
plain_genes = [set(pos) for pos in zip(*plain)]

print( spotty_genes )
print( plain_genes )

candidate_count = 0
for i, j, k in combinations(range(m), 3):
    # Build the set of 3‑tuples from the three spotty columns:
    spot_patterns = set(zip(
        spotty_genes[i],
        spotty_genes[j],
        spotty_genes[k],
    ))
    # And check for any overlap with the plain 3‑tuples:
    if spot_patterns.isdisjoint(zip(
        plain_genes[i],
        plain_genes[j],
        plain_genes[k],
    )):
        candidate_count += 1

print( candidate_count ) 

""" 
candidate_count = sum([
    1 
    for spos, ppos in zip(spotty_genes,plain_genes) 
    if spos.isdisjoint(ppos)
])

print( candidate_count ) 
"""