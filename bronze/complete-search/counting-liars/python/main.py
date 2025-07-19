n = int(input())

claims = [tuple(input().split()) for _ in range(n)]
claims = [(d,int(p)) for d, p in claims]

# this search space is to big if we try to test all possigle. 
# locations of the cow. we can reduce the space by recognizing that 
# there is no difference in liar count for any p that is between two
# claims.

search_space = {
    c + d 
    for _, c in claims 
    for d in (-1, 0, 1) 
    if c + d >= 0}

min_lies = len(claims)

for p in search_space:
    lies = 0
    for dir, pos in claims:
        if dir == "G" and p < pos:
            lies += 1
        if dir == "L" and p > pos:
            lies += 1
    min_lies = min(min_lies,lies)


print(min_lies)