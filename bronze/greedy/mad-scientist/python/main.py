with open("breedflip.in","r") as fin:
    N = int(fin.readline().strip())
    ordered = [c for c in fin.readline().strip()]
    received = [c for c in fin.readline().strip()]

i = 0
last = 1
count = 0
while i < N:
    current = 1 if ordered[i] == received[i] else 0
    count += (last and not current)
    last = current
    i += 1

with open("breedflip.out","w") as fout:
    print(count,file=fout)
