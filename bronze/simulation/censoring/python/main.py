with open("censor.in","r") as read:
    s = read.readline().strip()
    t = read.readline().strip()

stack = []
last_c = t[-1]
t_len = len(t)

for c in s:
    stack.append(c)

    if c == last_c and t_len <= len(stack):
        if "".join(stack[-t_len:]) == t:
            del stack[-t_len:]

with open("censor.out","w") as out:
    print("".join(stack),file=out)
