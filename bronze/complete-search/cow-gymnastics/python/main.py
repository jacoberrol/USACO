with open("gymnastics.in", "r") as fin:
    # K practice sessions. N cows
    k, n = map(int,fin.readline().split())
    lines = [list(map(int, fin.readline().split())) for _ in range(k)]

practices = [
    { val: idx for idx, val in enumerate(line)}
    for line in lines
]

pairs = {
    (x,y)
    for x in range(1,n+1)
    for y in range(x+1,n+1)
}

inconsistent = set()

for p in pairs:
    
    p0, p1 = 0, 0
    for session in practices:
        p0 += (session[p[0]] < session[p[1]])
        p1 += (session[p[1]] < session[p[0]])

    if p0 != 0 and p1 != 0:
        # not consistent, remove the pair
        inconsistent.add(p)

with open("gymnastics.out","w") as fout:
    print( len(pairs) - len(inconsistent), file=fout)
