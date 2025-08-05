with open("sleepy.in","r") as fin:
    N = int(fin.readline().strip())
    cows = tuple(reversed(list(map(int,fin.readline().split()))))

    ans = 0
    for i in range(1,N):
        if cows[i] > cows[i-1]:
            ans = N-i
            break

with open("sleepy.out","w") as fout:
    print(ans,file=fout)