
with open('input.txt') as f:
    signal = [line.strip('\n') for line in f]


def part_one(s):
  temp = ''
  if len(set(s[:4])) == 4:
    return 4
  else:
    temp += s[:4]
    for i in range(4, len(s)):
      temp += s[i]
      if len(set(temp[-4:])) == 4:
        return i+1
        
def part_two(s):
  temp = ''
  if len(set(s[:14])) == 14:
    return 14
  else:
    temp += s[:14]
    for i in range(14, len(s)):
      temp += s[i]
      if len(set(temp[-14:])) == 14:
        return i+1

print(part_one(signal[0]))
print(part_two(signal[0]))
    