import itertools

with open("lineup.in") as fin:
    N = int(fin.readline().strip())
    constraints = [
        (a, b) for a, _, _, _, _, b in 
        [tuple(fin.readline().strip().split()) for _ in range(N)]
    ]

cows = sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"])

def satisfies(ordering):
    pos = {cow: i for i, cow in enumerate(ordering)}
    return all(abs(pos[a] - pos[b]) == 1 for a, b in constraints)

for perm in itertools.permutations(cows):
    if satisfies(perm):
        with open("lineup.out", "w") as fout:
            fout.write("\n".join(perm) + "\n")
            break



