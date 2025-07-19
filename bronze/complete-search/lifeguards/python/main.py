with open("lifeguards.in","r") as fin:
    n = int(fin.readline().strip())
    shifts = [list(map(int,fin.readline().split())) for _ in range(n)]

output = 0

for skip in range(len(shifts)):
    covered = set()
    for n, (t0, t1) in enumerate(shifts):
        if n != skip:
            covered.update(set(range(t0,t1)))
            
    output = max(output,len(covered))

with open("lifeguards.out","w") as fout:
    print(output,file=fout)