
n = int(input())

xn = list(map(int,input().split()))
yn = list(map(int,input().split()))

out = 0

for n0 in range(0,n-1):
    for n1 in range(1,n):
        dx = abs(xn[n0] - xn[n1])
        dy = abs(yn[n0] - yn[n1])
        out = max(out,dx **2 + dy ** 2)

print(out)