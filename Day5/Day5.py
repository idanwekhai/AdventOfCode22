import re
from collections import defaultdict
with open('input.txt') as f:
    lines = [line.strip('\n') for line in f]

crates = lines[:8]
interval = list(range(0, len(crates[0]), 4))
stack = defaultdict(list)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

for i in range(len(crates)):
  line = crates[i]
  search = list(find_all(line, '['))
  for i in range(len(search)):
    pos = search[i]
    stack[interval.index(pos)+1].append(line[search[i]:search[i]+3])


instruction = [list(map(int, re.findall(r'\d+', i))) for i in lines[10:]]

def part_one(seq, instructions):
  seq = seq.copy()
  for i in instructions:
    top = seq[i[1]][:i[0]] #reverse and take ith top
    seq[i[1]] = seq[i[1]][i[0]:]
    seq[i[2]] = top[::-1] + seq[i[2]]
  answer = [seq[k][0][1] for k in range(1, len(seq)+1)]
  return ''.join(answer)

def part_two(seq, instructions):
   seq = seq.copy()
   for i in instructions:
     top = seq[i[1]][:i[0]] #reverse and take ith top
     seq[i[1]] = seq[i[1]][i[0]:]
     seq[i[2]] = top + seq[i[2]]
   answer = [seq[k][0][1] for k in range(1, len(seq)+1)]
   return ''.join(answer)

print(part_one(stack, instruction))
print(part_two(stack, instruction))
    