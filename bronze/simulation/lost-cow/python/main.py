
# lost cow submission
# https://usaco.org/index.php?page=viewproblem2&cpid=735
#

import math

with open("lostcow.in") as read:
    x, y = [int(x) for x in read.readline().strip().split()]


# x = farmer
# y = cow
#
# for each attempt until the last one where the farmer finds the cow
# the farmer must walk out and back to his original location, each time
# doubling the distance. we essentially add powers of two until the final 
# attempt which simply adds the straighline distance.

dist = abs(x - y)

# Figure out how many rounds are needed to pass the cow
pow = math.ceil(math.log2(dist))

# Check if we need an extra round to land on correct direction
if (    pow % 2 == 1 and y > x
    or  pow % 2 == 0 and y < x):
    pow += 1

total = (2 ** (pow + 1) - 2) + dist

print(total,file=open("lostcow.out","w"))
