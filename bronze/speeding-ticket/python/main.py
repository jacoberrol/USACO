# speeding ticket submission
# https://usaco.org/index.php?page=viewproblem2&cpid=568

with open("speeding.in") as read:
    n, m = map(int,read.readline().strip().split())
    limits = [tuple(map(int,read.readline().strip().split())) for _ in range(n)]
    speeds = [tuple(map(int,read.readline().strip().split())) for _ in range(m)]

    # Flatten segments into full mile-by-mile arrays
    speed_limit = [speed for length, speed in limits for _ in range(length)]
    speed_traveled = [speed for length, speed in speeds for _ in range(length)]

out = 0

for i in range(100):
    out = max(out,speed_traveled[i] - speed_limit[i])
        
print(out,file=open("speeding.out","w"))
