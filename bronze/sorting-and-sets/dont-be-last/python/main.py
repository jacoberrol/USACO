from collections import defaultdict

with open("notlast.in","r") as fin:
    N = int(fin.readline().strip())
    cows = [(name, int(m)) for name, m in (fin.readline().split() for _ in range(N))]

names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
acc = {name: 0 for name in names}
for name, amt in cows:
    acc[name] += amt

cows = list(acc.items())
cows.sort(key=lambda c: c[1])

amounts = sorted({amt for _, amt in cows})

ans = "Tie"
if len(amounts) > 1:
    next_min_amt = amounts[1]

    second_last = [name for name, amt in cows if amt == next_min_amt]

    if len(second_last) == 1:
        ans = second_last[0]

with open("notlast.out","w") as fout:
    print(ans,file=fout)