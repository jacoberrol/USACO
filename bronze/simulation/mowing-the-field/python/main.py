
def dir_tuple(d):
    if d == "N":
        return (0,1)
    elif d == "S":
        return (0,-1)
    elif d == "E":
        return (1,0)
    elif d == "W":
        return (-1,0)

with open("mowing.in") as read:
    n = int(read.readline())
    steps = [(d, int(s)) for d, s in (line.split() for line in read)]

t = 0
loc = (0,0)
path = dict()
path[loc] = t
mint = float("Inf")

for step in steps:
    d = dir_tuple(step[0])
    for s in range(step[1]):
        t += 1
        loc = tuple(a + b for a, b in zip(loc,d))
        if loc in path:
            t0 = path[loc]
            mint = min(t-t0,mint)
            path[loc] = t
        else:
            path[loc] = t
            
# no intersections, print -1
if mint == float("Inf"):
    mint = -1

with open("mowing.out","w") as out:
    print(mint,file=out)