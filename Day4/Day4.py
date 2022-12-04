with open('input.txt') as f:
    sections = [line.strip('\n').split(',') for line in f]

sections = [[list(map(int, i[0].split('-'))), list(map(int, i[1].split('-')))] for i in sections]

def part_one(seq):
  count = 0
  for item in seq:
    section_1 = set(range(item[0][0], item[0][1]+1))
    section_2 = set(range(item[1][0], item[1][1]+1))
    if (section_1.issuperset(section_2)) or (section_2.issuperset(section_1)):
      count += 1
  return count

def part_two(seq):
  count = 0
  for item in seq:
    section_1 = set(range(item[0][0], item[0][1]+1))
    section_2 = set(range(item[1][0], item[1][1]+1))
    if len(section_1.intersection(section_2)) != 0:
      count += 1
  return count


print(part_one(sections))
print(part_two(sections))
    