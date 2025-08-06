import math

with open("art.in","r") as fin:
    N = int(fin.readline().strip())
    canvas = [
        [int(c) for c in fin.readline().strip()]
        for _ in range(N)
    ]

LEFT, RIGHT, TOP, BOTTOM = 0, 1, 2, 3
INF = math.inf
MAX_COLORS = 9

def compute_bounding_boxes(canvas):
    bounding_boxes = [[INF,-1,INF,-1] for _ in range(MAX_COLORS+1)]

    colors = set()

    for i, row in enumerate(canvas):
        for j, val in enumerate(row):
            if val != 0:
                colors.add(val)
                box = bounding_boxes[val]
                box[LEFT] = min(box[LEFT],j)
                box[RIGHT] = max(box[RIGHT],j)
                box[TOP] = min(box[TOP],i)
                box[BOTTOM] = max(box[BOTTOM],i)

    return (colors,bounding_boxes)

def find_covering_colors(color,bounding_boxes,canvas):
    covering_colors = set()
    left, right, top, bottom = bounding_boxes[color]
    for i in range(top,bottom+1):
        for j in range(left,right+1):
            if canvas[i][j] != color:
                covering_colors.add(canvas[i][j])
    return covering_colors

colors, bounding_boxes = compute_bounding_boxes(canvas)

covering_colors = set().union(*[
    find_covering_colors(c, bounding_boxes, canvas) for c in colors
])

bottom_colors = colors - covering_colors

with open("art.out","w") as fout:
    print(len(bottom_colors),file=fout)