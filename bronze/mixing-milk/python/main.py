
read = open("mixmilk.in")

buckets = []

for _ in range(3):
    c, m = [int(i) for i in read.readline().split()]
    buckets.append([c,m])

print(f"initial state: {buckets}")

for i in range(100):
    i1 = i%3
    i2 = (i+1)%3

    x = buckets[i2][0] - buckets[i2][1] # excess capacity in next bucket
    p = min(buckets[i1][1], x)          # how much to pour

    buckets[i1][1] -= p
    buckets[i2][1] += p

    print(f"pour {p} from {i1} to {i2}")
    print(f"{i} state: {buckets}")

outfile=open("mixmilk.out", "w")
for i in range(3):
    print(buckets[i][1],file=outfile)