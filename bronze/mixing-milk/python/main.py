N=3
TURNS=100

read = open("mixmilk.in")

capacity = [0 for _ in range(N)]
milk = [0 for _ in range(N)]

with open("mixmilk.in","r") as read:
    for i in range(N):
        capacity[i], milk[i] = map(int, read.readline().split())

print(f"initial state: {capacity}, {milk}")

for i in range(TURNS):
    b1 = i%N
    b2 = (i+1)%N

    p = min(milk[b1], capacity[b2] - milk[b2]) # how much to pour

    milk[b1] -= p
    milk[b2] += p

    print(f"pour {p} from {b1} to {b2}")
    print(f"{i} state: {milk}")

with open("mixmilk.out", "w") as out:
    for m in milk:
        print(m,file=out)