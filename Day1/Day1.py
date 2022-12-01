with open('input.txt') as f:
    numbers = [line.strip('\n') for line in f]

def find_max_calories(numbers):
  cal_counts = []   
  count = 0
  for i in range(0, len(numbers)):
    if numbers[i] != '':
      count += int(numbers[i])
    else:
      cal_counts.append(count)
      count = 0
  return max(cal_counts)

def find_top_three_calories(numbers):
  cal_counts = []   
  count = 0
  for i in range(0, len(numbers)):
    if numbers[i] != '':
      count += int(numbers[i])
    else:
      cal_counts.append(count)
      count = 0
  return sum(sorted(cal_counts, reverse=True)[:3])
  
  
print("1", find_max_calories(numbers))
print("2", find_top_three_calories(numbers))
