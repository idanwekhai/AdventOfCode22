import numpy as np
with open('input.txt') as f:
    trees = [line.strip('\n') for line in f]

tree = np.array([list(map(int, j)) for j in [[*i] for i in trees] ])

def part_one(seq):
  count = 0
  edge = len(seq)-1
  for i in range(len(seq)):
    for j in range(len(seq)):
      if i == 0 or j==0:
        count += 1
      elif i == edge or j == edge:
        count += 1
      else:
        c = seq[i,j]
        if (c > max(seq[:i,j])) or (c > max(seq[i,:j])) or (c > max(seq[i+1:,j])) or (c > max(seq[i,j+1:])):
          count += 1
  return count


def scenic_counter(num, arr):
  count = 0
  i = 0
  if arr[0] > num or arr[0] == num:
    return 1
  elif max(arr)<num:
    return len(arr)
  else:
    while arr[i]<num:
      count+=1
      i+=1
    return count+1

def part_two(seq):
  scenic_scores = []
  edge=len(seq)-1
  for i in range(len(seq)):
    for j in range(len(seq)):
      if i ==0 or j == 0 or i == edge or j == edge:
        pass
      else:
        c = seq[i,j]
        up = np.flipud(seq[:i,j])
        right  = np.flipud(seq[i,:j])
        down = seq[i+1:,j]
        left = seq[i,j+1:]
        up_count = scenic_counter(c, up)
        right_count = scenic_counter(c, right)
        down_count = scenic_counter(c, down)
        left_count = scenic_counter(c, left)
        scenic_scores.append(up_count*right_count*down_count*left_count)
  print(scenic_scores)
  return max(scenic_scores)

print(part_one(tree))
print(part_two(tree))
