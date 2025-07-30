with open("measurement.in","r") as read:
    n = int(read.readline())
    measurements = [[int(day), cow, int(change)] for day, cow, change in (read.readline().split() for _ in range(n))]

measurements.sort(key=lambda c: c[0])

current = {
    "Mildred": 7,
    "Elsie": 7,
    "Bessie": 7
}

leader_board = set(["Mildred","Elsie","Bessie"])

leader_change = 0

for m in measurements:
    # apply measurement
    current[m[1]] += m[2]

    # find the current highest value
    max_v = max(current.values())

    # find all keys associated with the highest value.
    new_leader = set([k for k, v in current.items() if v == max_v])

    if new_leader != leader_board:
        leader_change += 1

    leader_board = new_leader

with open("measurement.out","w") as out:
    print(leader_change,file=out)