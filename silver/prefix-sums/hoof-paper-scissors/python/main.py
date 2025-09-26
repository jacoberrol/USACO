with open("hps.in","r") as fin:
    N = int(fin.readline().strip())
    GAMES = [""] + list(fin.readline().strip() for _ in range(N)) + [""]

def psum(win,arr,i):
    arr[i] = arr[i-1] + (1 if GAMES[i] == win else 0)

def rsum(win,arr,i):
    arr[i] = arr[i+1] + (1 if GAMES[i+1] == win else 0)

def max_win(first,second):
    return max((f+s) for f, s in zip(first,second))

ps_h, ps_p, ps_s = [0]*(N+1), [0]*(N+1), [0]*(N+1)
rs_h, rs_p, rs_s = [0]*(N+1), [0]*(N+1), [0]*(N+1)

for i in range(1,N+1):
    psum("S",ps_h,i)
    psum("H",ps_p,i)
    psum("P",ps_s,i)

    rsum("S",rs_h,N-i)
    rsum("H",rs_p,N-i)
    rsum("P",rs_s,N-i)

ans = max([
    max_win(ps_h, rs_p),
    max_win(ps_h, rs_s),
    max_win(ps_p, rs_h),
    max_win(ps_p, rs_s),
    max_win(ps_s, rs_h),
    max_win(ps_s, rs_p)
])

with open("hps.out","w") as fout:
    print(ans,file=fout)