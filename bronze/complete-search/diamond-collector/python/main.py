
with open("diamond.in","r") as read:
    n, k = map(int,read.readline().split())
    diamonds = [int(d.strip()) for d in read]

# sort the diamonds in order of ascending size
diamonds.sort()

max_diamonds = 0

result = 0
# start with the largest possible window
# and work backward
for length in reversed(range(n)):
    # test each possible placement of the largest window
    for start in range(0,n-length):
        if diamonds[start+length] - diamonds[start] <= k:
            result = length
            break
    if result > 0:
        break

with open("diamond.out","w") as out:
    print(result+1,file=out)
        
