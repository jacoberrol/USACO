
with open("pails.in","r") as read:
    x, y, m = map(int,read.readline().split())


max_x = int(m/x)
max_y = int(m/y)

best = 0

for xi in range(m // x + 1):
    rem = m - xi * x
    yi = rem // y
    total = xi * x + yi * y
    if total > best:
        best = total

with open("pails.out","w") as out:
    print(best,file=out)
