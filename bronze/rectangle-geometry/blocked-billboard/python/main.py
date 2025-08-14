with open("billboard.in","r") as fin:
    ax1, ay1, ax2, ay2 = map(int,fin.readline().split())
    bx1, by1, bx2, by2 = map(int,fin.readline().split())
    tx1, ty1, tx2, ty2 = map(int,fin.readline().split())

line_overlap = lambda a1, a2, b1, b2: max(0,min(a2,b2) - max(a1,b1))
rect_overlap = lambda pa1, pa2, pb1, pb2: line_overlap(pa1[0],pa2[0],pb1[0],pb2[0]) * line_overlap(pa1[1],pa2[1],pb1[1],pb2[1])

o1 = rect_overlap((ax1,ay1),(ax2,ay2),(tx1,ty1),(tx2,ty2))
o2 = rect_overlap((bx1,by1),(bx2,by2),(tx1,ty1),(tx2,ty2))

ans = ((ay2-ay1) * (ax2 - ax1) + (by2-by1) * (bx2-bx1)) - (o1+o2)

with open("billboard.out","w") as fout:
    print(ans,file=fout)
