with open("taming.in","r") as fin:
    N = int(fin.readline().strip())
    log = tuple(map(int,fin.readline().split()))

total_days = len(log)
known_breakouts = {0}
known_quiet_days = set()

for i, e in enumerate(log):
    if e >= 0 and i > e:
        known_breakouts.add(i-e)
    if e > 0:
        for j in range(i-e+1,i+1):
            known_quiet_days.add(j)

min = len(known_breakouts)
max = total_days - len(known_quiet_days)

with open("taming.out","w") as fout:
    if min > max:
        print(f"{-1}",file=fout)
    else:
        print(f"{min} {max}",file=fout)