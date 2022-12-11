from collections import defaultdict, OrderedDict
import math
with open('input.txt') as f:
    actions = [line.strip('\n').strip('').split() for line in f]
    actions = [i for i in actions if len(i)!=0]

scenario = []
for i in range(8):
  scenario.append(actions[i*6:(6*i)+6])

monkey_counts = defaultdict(int)
monkey_poss = OrderedDict()
for monkey in scenario:
  monkey_no = int(monkey[0][1][0])
  starting_items = list(map(int, [i.strip(',') for i in monkey[1][2:]]))
  operation =  monkey[2][3:]
  divisible_by = int(monkey[3][3])
  if_true = int(monkey[4][-1])
  if_false = int(monkey[5][-1])
  monkey_poss[monkey_no] = [starting_items, operation, divisible_by, if_true, if_false]

def part_one(seq):
  monkey_counts = defaultdict(int)
  for i in range(20):
    for k, v in monkey_poss.items():
      monkey_poss[k]
      if len(monkey_poss[k][0]) != 0:
        to_del = []
        for i in range(len(monkey_poss[k][0])):
          old = monkey_poss[k][0][i]
          monkey_counts[k]+=1
          level = math.floor(eval(''.join(monkey_poss[k][1]))/3)
          if level % monkey_poss[k][2] == 0:
            monkey_poss[monkey_poss[k][3]][0].append(level)
            to_del.append(monkey_poss[k][0][i])
          else:
            monkey_poss[monkey_poss[k][4]][0].append(level)
            to_del.append(monkey_poss[k][0][i])
        for i in to_del:
          monkey_poss[k][0].remove(i)
  ans = math.prod(sorted([v for k,v in monkey_counts.items()])[-2:])
  return ans

        
def part_two(seq,  monkey_counts = defaultdict(int)):
  # monkey_counts = defaultdict(int)

  for i in range(10000):
    for k, v in monkey_poss.items():
      monkey_poss[k]
      if len(monkey_poss[k][0]) != 0:
        to_del = []
        for i in range(len(monkey_poss[k][0])):
          old = monkey_poss[k][0][i]
          monkey_counts[k]+=1
          level = eval(''.join(monkey_poss[k][1]))
          # level = math.floor(eval(''.join(monkey_poss[k][1]))/3)
          if level % monkey_poss[k][2] == 0:
            monkey_poss[monkey_poss[k][3]][0].append(level)
            to_del.append(monkey_poss[k][0][i])
          else:
            monkey_poss[monkey_poss[k][4]][0].append(level)
            to_del.append(monkey_poss[k][0][i])
        for i in to_del:
          monkey_poss[k][0].remove(i)
  ans = math.prod(sorted([v for k,v in monkey_counts.items()])[-2:])
  return ans


# print(part_one(scenario))
print(part_two(scenario))