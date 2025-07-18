n = int(input())
flowers = list(map(int,input().split()))

count = len(flowers)
for i in range(n):
    pi = flowers[i]
    total = pi
    seen = {pi}
    for j in range(i+1,n):
        pj = flowers[j]
        total += pj
        seen.add(pj)
        length = j - i + 1

        if total % length == 0 and (total // length) in seen:
            count += 1

print(count)