from collections import defaultdict

with open("circlecross.in","r") as fin:
    circle = [p for p in fin.readline().strip()]

stack = list()
encountered = set()
crossing_pairs = set()

for p in circle:
    if not p in encountered:
        stack.append(p)
        encountered.add(p)
    else:
        crossed = list()
        while stack[-1] != p:
            crossed.append(stack.pop())
        stack.pop()
        
        crossing_pairs.update([tuple(sorted((p,c))) for c in crossed])
        
        while len(crossed) > 0:
            stack.append(crossed.pop())

with open("circlecross.out","w") as fout:
    print(len(crossing_pairs),file=fout)