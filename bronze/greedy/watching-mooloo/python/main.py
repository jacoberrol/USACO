N, K = map(int,input().split())
days = list(map(int,input().split()))

subscr = K+1

for i in range(1,N):
    diff = days[i] - days[i-1]
    if diff <= K:
        subscr += diff
    else:
        subscr += K+1

print(subscr)