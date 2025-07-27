# greedy algorithm to count the minimum number, c, of combinations required
# to convert p, at an array [m,m,...,m] = pc. where len(pc) == len(p) - c
# return 0 if no moves are required and -1 if it is impoossible to arrive
# a solution, otherwise return c.
def greedy(m,p):
    i, j, c = 0, 0, 0
    while i < len(p):
        if p[i] == m:
            i+=1
            continue
        elif p[i] > m:
            return -1
        else:
            j = i+1
            tmp = p[i]
            while j < len(p) and tmp < m:
                tmp += p[j]
                c += 1
                j+=1
            if tmp == m:
                i = j
            else:
                return -1
    return c

#
# the main program starts here
#
classes = list()

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    classes.append(list(map(int,input().strip().split())))

for periods in classes:
    out = len(periods)-1
    s = sum(periods)
    if s == 0:
       out = 0
    else:
        factors = [f for f in range(2,s//2 + 1) if s % f == 0]

        for f in factors:
            c = greedy(f,periods)
            if c >= 0:
                out = c
                break
            
    print(out)


