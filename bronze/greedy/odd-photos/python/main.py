N = int(input().strip())
breeds = list(map(int,input().split()))

odd = sum(b % 2 for b in breeds)
even = N-odd
ans = even*2
if even > odd:
    ans = (odd*2 + 1)
elif odd > even:
    ans += 2*((odd-even)//3)
    if (odd-even)%3 == 1:
        ans -= 1
    elif (odd-even)%3 == 2:
        ans += 1

print(ans)