with open("cbarn.in","r") as read:
    n = int(read.readline())
    rooms = [int(read.readline()) for _ in range(n)]

total_cows = sum(rooms)
best_cost = float('inf')

for start in range(n):
    cows_remaining = total_cows - rooms[start]
    walking_cost = 0
    for offset in range(1,n):
        room_index = (start + offset) % n
        walking_cost += cows_remaining
        cows_remaining -= rooms[room_index]
    
    best_cost = min(best_cost,walking_cost)

with open("cbarn.out","w") as out:
    print(best_cost,file=out)