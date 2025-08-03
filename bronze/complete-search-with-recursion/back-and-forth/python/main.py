from functools import lru_cache

with open("backforth.in","r") as fin:
    barn1 = tuple(map(int,fin.readline().strip().split()))
    barn2 = tuple(map(int,fin.readline().strip().split()))

@lru_cache(maxsize=None)
def solve(n, barn1, barn2):

    def canonical(barn):
        return tuple(sorted(barn))

    if n == 4:
        return {sum(barn1)}
    
    ans = set()

    for b in set(barn1):
        b1, b2 = list(barn1), list(barn2)
        b1.remove(b)
        b2.append(b)
        ans |= solve(n+1,canonical(b2),canonical(b1))

    return ans

ans = solve(0, barn1, barn2)

with open("backforth.out","w") as fout:
    print(len(ans),file=fout)