with open('input.txt') as f:
    rack = [line.strip('\n') for line in f]

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = range(1, 53)
priority_map = dict(zip(alphabets, priority))

def part_one(seq):
  count = 0
  for item in seq:
    first_half = set(item[:int(len(item)/2)])
    second_half = set(item[int(len(item)/2):])
    common = first_half.intersection(second_half).pop()
    count += priority_map[common]
  return count

def part_two(seq):
  count = 0
  for i in range(1, len(seq)+1):
    if i % 3 == 0:
      first = set(seq[i-3])
      second = set(seq[i-2])
      third = set(seq[i-1])
      common = first.intersection(second).intersection(third).pop()
      count += priority_map[common]
  return count


print(part_one(rack))
print(part_two(rack))
    