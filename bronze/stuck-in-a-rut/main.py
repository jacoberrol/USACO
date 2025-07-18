
def filter_cows(cows,dir):
    return [
        (x, y, i)
        for i, (d, x, y) in enumerate(cows)
        if d == dir
    ]

n = int(input())
cows = [[d, int(x), int(y)] for d, x, y in (input().strip().split() for _ in range(n))]

north_cows = filter_cows(cows,"N")
north_cows.sort(key=lambda c: c[0])   # sort by x ascending

east_cows = filter_cows(cows,"E")
east_cows.sort(key=lambda c: c[1])    # sort by y ascending

INF = float("Inf")
distance = [INF] * n

for ex, ey, ei in east_cows:
    for nx, ny, ni in north_cows:

        ix, iy = nx, ey

        # we only evaluate if the intersection is 
        # north east of both points
        if ix > ex and iy > ny:
            dX = ix - ex
            dY = iy - ny

            # only record this new intersection if it is
            # closer than a previously recorded intersection
            if dX < distance[ei] and dY < distance[ni]:

                # if the x distance is smaller than y, then N stops
                if dX < dY:
                    distance[ni] = dY

                # if the y distance is smaller than x, then E stops        
                if dY < dX:
                    distance[ei] = dX


for d in distance:
    if d == INF:
        print("Infinity")
    else:
        print(d)