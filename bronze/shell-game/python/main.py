
read = open("shell.in")

n = int(read.readline())

print(f"there are {n} lines")

# number the shells 0, 1, 2 and place them in their starting position
shell_at = [0,1,2]

# count the number of times a particular shell was guessed
counter = [0 for _ in range(n)]

for i in range(n):
    # get the next line of input
    a, b, g = [int(i) - 1 for i in read.readline().split()]

    print(f"swap ({a},{b}) and guess {g}")

    # simulate the swap
    shell_at[a], shell_at[b] = shell_at[b], shell_at[a]

    # increment the counter for the shell (not the position!)
    counter[ shell_at[g] ] += 1

m = max(counter)
print(f"max correct guesses is {m}")

print(m, file=open("shell.out", "w"))
