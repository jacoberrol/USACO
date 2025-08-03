
from functools import lru_cache
from itertools import accumulate


N, M = map(int,input().strip().split())

cows_in = [tuple(map(int,input().strip().split())) for _ in range(N)]
acs_in = [tuple(map(int,input().strip().split())) for _ in range(M)]

cows = [(s-1, t, c) for s, t, c in cows_in]
acs = [(a-1, b, p, m) for a, b, p, m in acs_in]

last_stall = max(
    max([end for _, end, _ in cows]),
    max([end for _, end, _, _ in acs])
)

stalls = [
    next((temp for start, end, temp in cows if start <= i < end ),0)
    for i in range(last_stall)
]

def solve():
    S = len(stalls)
    INF = 10 ** 9

    @lru_cache(None)
    def rec(n, ison, total_cost, diff):
 
        if n == len(acs):
            return total_cost
        
        start, end, temp, cost = acs[n]
        
        if ison:
            total_cost += cost
            diff_list = list(diff)
            diff_list[start] += temp
            diff_list[end] -= temp
            diff = tuple(diff_list)

        max_temp = max(
            [ a - b for a, b in (zip(stalls, accumulate( diff[:S] )))]
        )

        if max_temp <= 0:
            return total_cost
        elif n == len(acs) - 1:
            return INF
        else:
            return min(
                rec(n+1, 0, total_cost, diff),
                rec(n+1, 1, total_cost, diff)
            )
        
    diff = tuple([0] * (S+1))
    
    return min(
        rec(0, 0, 0, diff),
        rec(0, 1, 0, diff)
    )

print(solve())
