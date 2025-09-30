import itertools

N = int(input())
x = list(map(int,input().split()))

# print(x)

current_sum = x[0]
max_subarray_sum = x[0]

# print(f"0: {current_sum} {max_subarray_sum}")

for i in range(1,N):
    current_sum = max(current_sum + x[i], x[i])    
    max_subarray_sum = max(max_subarray_sum, current_sum)
    # print(f"{i}: {current_sum} {max_subarray_sum}")

print(max_subarray_sum)