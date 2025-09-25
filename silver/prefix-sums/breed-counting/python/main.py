import itertools

with open("bcount.in","r") as fin:
    N, Q = map(int,fin.readline().split())
    cows = [int(fin.readline().strip()) for _ in range(N)]
    queries = [tuple(map(int,fin.readline().split())) for _ in range(Q)]

def psum(n):
    return [0] + list(itertools.accumulate([1 if c == n else 0 for c in cows]))

ps_1, ps_2, ps_3 = psum(1), psum(2), psum(3)

with open("bcount.out","w") as fout:
    for a, b in queries:
        print(f'{ps_1[b] - ps_1[a-1]} {ps_2[b] - ps_2[a-1]} {ps_3[b] - ps_3[a-1]}',file=fout)



'''

print(f'{N} {Q}')
print(f'{cows}')
print(f'{queries}')

print(f'{ps_1}')
print(f'{ps_2}')
print(f'{ps_3}')
6 3
2
1
1
3
2
1
1 6
3 3
2 4

0 1 2 3 4 5
0 1 1 0 0 1
0 1 2 2 2 3
'''