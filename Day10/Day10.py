with open('Day10/input.txt') as f:
    cmds = [line.strip('\n').split(' ') for line in f]


# def part_one(seq):
#   cycles = [(1,1)]
#   x=1
#   count = 0
#   cycle=0
#   pending = []
#   for i in range(1, len(seq)+1):
#     if seq[i-1][0] == 'addx':
#       val = int(seq[i-1][1])
#       if cycle == 2:
        
#         adding = pending[0]
#         pending = pending[1:]
#         x+=adding
#         cycles.append((count+2, x))
#         pending.append(val)
#         cycle = 2
#         count+=2
#       else:
#         pending.append(val)
#         cycle+=1
#         count+=1
#     elif seq[i-1][0] == 'noop':
#       if cycle == 2:
#         if len(pending) > 1:
#           adding = pending[0]
#           pending = pending[1:]
#           x+=adding
#           cycles.append((count+2, x))
#         # pending.append(val)
#           count+=2
#           cycle=2
#       else:
#         cycle=1
#         count+=1
#         # cycles.append((cycle+1, x))
#     print(f'{cycle} - {count} - {x}')
#   return cycles

def part_one(seq):
  needed = [20,60,100,140,180,220]
  x=1
  counter=1
  total = 0
  for i in range(1, len(seq)):
    counter +=1
    if seq[i-1][0] == 'addx':
      total +=(counter*x if counter in needed else 0)
      val = int(seq[i-1][1])
      counter += 1
      x+=val
    total +=(counter*x if counter in needed else 0)
  return total

        
def part_two(seq):
  x=1
  counter=0
  output = []
  blink_pos = [0,1,2]
  for i in range(1, len(seq)):
    for j in range(2 if seq[i-1][0] == 'addx' else 1):
      output.append('#' if counter in blink_pos else '.')
      counter = (counter+1) % 40
      blink_pos = [j + int(seq[i-1][1]) for j in blink_pos] if j==1 else blink_pos
  for r in range(6):
    print(''.join(output[r*40:(r+1)*40]))


# print(cmds)
print(part_one(cmds))
print(part_two(cmds))