from collections import Counter

with open("blocks.in", "r") as read:
    n = int(read.readline())
    blocks = [tuple(read.readline().strip().split()) for _ in range(n)]

result = [0] * 26

for a, b in blocks:
    count_a = Counter(a)
    count_b = Counter(b)
    for i in range(26):
        ch = chr(ord('a') + i)
        result[i] += max(count_a.get(ch, 0), count_b.get(ch, 0))

with open("blocks.out", "w") as out:
    for count in result:
        print(count, file=out)