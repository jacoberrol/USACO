
from collections import Counter

with open("tttt.in","r") as read:
    board = [list(read.readline().strip()) for _ in range(3)]

lines = []

# rows
lines.extend(board)

# columns
lines.extend([[board[0][i],board[1][i],board[2][i]] for i in range(3)])

# diagonals
lines.append([board[0][0],board[1][1],board[2][2]])
lines.append([board[2][0],board[1][1],board[0][2]])

individual_winners = set()
team_winners = set()

def check_line(line):
    c = Counter(line)
    if len(c) == 1:
        individual_winners.add(line[0])
    elif len(c) == 2:
        team_winners.add(frozenset(c.keys()))


for line in lines:
    check_line(line)

with open("tttt.out","w") as out:
    print(len(individual_winners),file=out)
    print(len(team_winners),file=out)
