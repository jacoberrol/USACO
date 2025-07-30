
def process(segments, reverse=False):
    if reverse:
        segments = list(reversed(segments))

    minmax = [0,1000]

    for s, l, h in segments:
        if s == 'on' and not reverse or s=='off' and reverse:
            minmax[0] += l
            minmax[1] += h
        elif s == 'off' and not reverse or s=='on' and reverse:
            minmax[0] -= h
            minmax[1] -= l
        elif s == 'none':
            minmax[0] = max(minmax[0],l)
            minmax[1] = min(minmax[1],h)
    
        minmax[0] = max(minmax[0], 0)
        minmax[1] = max(minmax[1], minmax[0])
    
    return minmax

with open("traffic.in","r") as read:
    n = int(read.readline())
    segments = [
        (parts[0], int(parts[1]), int(parts[2]))
        for parts in (line.strip().split() for line in read)
    ]
    
before = process(segments,True)
after = process(segments,False)

with open("traffic.out","w") as out:
    print(f"{before[0]} {before[1]}",file=out)
    print(f"{after[0]} {after[1]}",file=out)

