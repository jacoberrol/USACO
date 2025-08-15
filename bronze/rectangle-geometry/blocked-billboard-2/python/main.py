with open("billboard.in") as fin:
    lx1, ly1, lx2, ly2 = map(int, fin.readline().split())  # lawnmower
    fx1, fy1, fx2, fy2 = map(int, fin.readline().split())  # feed (truck)

Lx = (lx1, lx2);  Ly = (ly1, ly2)
Fx = (fx1, fx2);  Fy = (fy1, fy2)

def span(seg):          # length of a 1D segment (x1,x2) or (y1,y2)
    return abs(seg[1] - seg[0])

def overlap(a, b):      # 1D overlap length of segments a and b
    return max(0, min(a[1], b[1]) - max(a[0], b[0]))

def spans(a, b):        # does b cover a completely along this axis?
    return overlap(a, b) >= span(a)

def touches_edge(a, b): # does b's overlap touch either endpoint of a?
    return b[0] <= a[0] or b[1] >= a[1]

LW, LH = span(Lx), span(Ly)
XO, YO = overlap(Lx, Fx), overlap(Ly, Fy)

ans = LW * LH
if spans(Lx, Fx) and spans(Ly, Fy):
    ans = 0
elif spans(Lx, Fx) and touches_edge(Ly, Fy):
    ans = LW * (LH - YO)   # single vertical strip remains
elif spans(Ly, Fy) and touches_edge(Lx, Fx):
    ans = LH * (LW - XO)   # single horizontal strip remains


with open("billboard.out", "w") as fout:
    print(ans, file=fout)
