
def do_shuffle(cin, shuffle):
    return [cin[v - 1] for v in shuffle]

with open("shuffle.in") as read:
    n = int(read.readline().strip())
    shuffle = list(map(int,read.readline().strip().split()))
    cows = list(map(int,read.readline().strip().split()))

for _ in range(3):
    cows = do_shuffle(cows, shuffle)

with open("shuffle.out","w") as out:
    for c in cows:
        print(c,file=out)
