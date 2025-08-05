from collections import defaultdict, deque

years = {
    "Ox": 0, "Tiger": 1, "Rabbit": 2, "Dragon": 3, 
    "Snake": 4, "Horse": 5, "Goat": 6, "Monkey": 7, 
    "Rooster": 8, "Dog": 9, "Pig": 10, "Rat": 11
}

N = int(input().strip())
constraints = [
    (name1, rel, years[year], name2)
    for _ in range(N)
    for name1, _, _, rel, year, _, _, name2
    in [input().split()]
]

def offset(rel, y0, y1):
    if rel == "next":
        d = (y1 - y0) % 12
        return d or 12
    else:
        d = (y0 - y1) % 12
        return -(d or 12)

constraint_map = defaultdict(list)
for x in constraints:
    constraint_map[x[3]].append(x)

ans = {"Bessie": (0, 0)}
q = deque(["Bessie"])

def apply_constraints(name,y0,t0):
    for child, rel, y1, _ in constraint_map[name]:
        if child not in ans:
            ans[child] = (y1, t0 + offset(rel,y0,y1))
            q.append(child)
  
while q:
    name = q.popleft()
    y0, t0 = ans[name]
    apply_constraints(name,y0,t0)

print(abs(ans["Elsie"][1]))
