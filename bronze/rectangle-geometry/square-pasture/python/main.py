with open("square.in","r") as fin:
    ax1, ay1, ax2, ay2 = map(int,fin.readline().split())
    bx1, by1, bx2, by2 = map(int,fin.readline().split())

xs = (ax1,ax2,bx1,bx2)
ys = (ay1,ay2,by1,by2)

max_edge = max(max(xs) - min(xs), max(ys) - min(ys))

with open("square.out","w") as fout:
    print(max_edge**2,file=fout)