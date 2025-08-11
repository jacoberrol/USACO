N = int(input().strip())
s = [1 if c == 'G' else 0 for c in input().strip()]

ans = 0
parity = 0 

for odd, even in zip(s[-2::-2], s[::-2]):
    need = (odd ^ parity) & (odd ^ even)
    ans += need
    parity ^= need

print(ans)
