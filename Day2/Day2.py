with open('Day2/input.txt') as f:
    strategy = [line.strip('\n').split() for line in f]

#A=ROCK, B=PAPER, C=SCISSORS
#X=ROCK, Y=PAPER, Z=SCISSORS

score_map_opponent = {'A':1, 'B':2, 'C':3}
score_map_player = {'X':1, 'Y':2, 'Z':3}
game_points = {'win':6, 'lose':0, 'draw':3}

draw = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
win = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
lose = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]

part_two_map = {'X':lose, 'Y':draw, 'Z':win}

def rock_paper_scissors(seq):
  if seq in draw:
    return 'draw'
  if seq in win:
    return 'win'
  if seq in lose:
    return 'lose'

def part_one(seq):
  total = 0
  for i in seq:
    first_point = score_map_player[i[1]]
    second_point = game_points[rock_paper_scissors(i)]
    round = first_point + second_point
    total += round
  return total

def part_two(seq):
  total = 0
  for i in seq:
   strategy = part_two_map[i[1]]
   for j in strategy:
     if j[0] == i[0]:
       decision = j
   first_point = score_map_player[decision[1]]
   second_point = game_points[rock_paper_scissors(decision)]
   round  = first_point + second_point
   total += round
  return total
    

print(part_one(strategy))
print(part_two(strategy))