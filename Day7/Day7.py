from collections import defaultdict
import sys
sys.setrecursionlimit(6000)
with open('input.txt') as f:
    cmds = [line.strip('\n').split(' ') for line in f]

counts = defaultdict(int)

folders = []
tree = defaultdict(list)
# tree = defaultdict(dict)

def part_one(seq, folder='/', out='/'):
  # folder = ''
  # out = ''
  for cmd in range(len(seq)):
    if seq[cmd][0] == '$':
      if seq[cmd][1] == 'cd':
        if seq[cmd][2] == '..':
          current = folder
          folder = out
          c_out = 0
          #out = '/'#folders[folders.index(current)-1]#folders[newfolder-1]
          for k, v in tree.items():
            if current in v:
              if len(tree[k]) > c_out: out = k
              else : c_out = len(tree[k])
        else:
          out = folder
          newfolder = seq[cmd][2]
          folder = newfolder
          folders.append(folder)
      elif seq[cmd][1] == 'ls':
        pass
    else:
      if seq[cmd][0] == 'dir':
        tree[folder].append(seq[cmd][1])
        for k, v in tree.items():
          if folder in v:
            tree[k].append(seq[cmd][1])
      else:
        if folder in counts.keys():
          counts[folder] += int(seq[cmd][0])
          for k,v in tree.items():
            if folder in v:
              counts[k] += int(seq[cmd][0])
        else:
          counts[folder] = int(seq[cmd][0])
          for k,v in tree.items():
            if folder in v:
              counts[k] += int(seq[cmd][0])
  print(out)
  ans = [v for k,v in counts.items() if v<=100000]
  return sum(ans)
        
        
def part_two(seq):
  pass


print(part_one(cmds))
print(part_two(cmds))