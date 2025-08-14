with open("paint.in","r") as fin:
    A, B = map(int,fin.readline().split())
    C, D = map(int,fin.readline().split())

ans = (B-A) + (D-C) - max(0,min(B,D) - max(A,C))

with open("paint.out","w") as fout:
    print(ans,file=fout)