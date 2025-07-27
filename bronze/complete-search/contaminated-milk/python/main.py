with open("badmilk.in","r") as fin:
    N, M, D, S = map(int,fin.readline().split())
    drinks = [tuple(map(int,fin.readline().split())) for _ in range(D)]
    sick_time = dict(tuple(map(int,fin.readline().split())) for _ in range(S))

candidate_milk = set.intersection(
    *({m  for (drinker, m, t) in drinks 
          if drinker == sick_person and t < sick_time[sick_person]}
          for sick_person in sick_time)
) if sick_time else set()

candidate_people = {p for  (p, m, t) in drinks if m in candidate_milk}

doses = len(candidate_people)

with open("badmilk.out","w") as fout:
    print(doses,file=fout)