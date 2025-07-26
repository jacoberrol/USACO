with open("balancing.in","r") as fin:
    N, B = map(int,fin.readline().split())
    cows = [tuple(map(int,fin.readline().split())) for _ in range(N)]

xs = {x + 1 for x, _ in cows}
ys = {y + 1 for _, y in cows}

ans = N
for a in xs:
    for b in ys:
        bl = tl = br = tr = 0
        for x, y in cows:
            if x < a:
                if y < b:
                    bl += 1
                else:
                    tl += 1
            else:
                if y < b:
                    br += 1
                else:
                    tr += 1

        ans = min(ans,max(bl,tl,br,tr))

with open("balancing.out","w") as fout:
    print(ans,file=fout)