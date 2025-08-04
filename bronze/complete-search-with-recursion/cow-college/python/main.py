N = int(input().strip())
can_pay = sorted(map(int,input().split()))

best_revenue, best_price = max(
    ((price * (N-i),price) for i, price in enumerate(can_pay)),
    key=lambda rp: (rp[0],-rp[1])
)

print(f"{best_revenue} {best_price}")