import re

f = open('in/t', 'r')
# f = open('in/i5', 'r')
lines = f.read().splitlines()
f.close()

def isIn(num, start,length):
  return true if num>=start and num<start+length else false

def part1():
  step = 0
  seeds = list(map(lambda a:list((a,0)), map(int, lines[0].split(": ")[1].split())))
  for line in lines[1:]:
    line=line.split()
    if len(line)==3:
      line=list(map(int,line))
      for seed in seeds:
        if step>seed[1]:
          if seed[0] >=line[1] and seed[0] <line[1]+line[2]:
            seed[0]+=line[0]-line[1]
            seed[1]+=1
    elif len(line)==2:
      seeds=list(map(lambda a: list((a[0],step)),seeds))
      step+=1
  print(min(seeds))
  
def zad2():
  step = 0
  # seeds = list(map(lambda a:list((a,0)), map(int, lines[0].split(": ")[1].split())))
  two=list(map(int, lines[0].split(": ")[1].split()[:2]))
  print(list(range(two[0],two[0]+two[1])))
  seeds = list(map(lambda a:list((a,0)), map(int, lines[0].split(": ")[1].split()[:2])))
  for line in lines[1:]:
    line=line.split()
    if len(line)==3:
      line=list(map(int,line))
      for seed in seeds:
        if step>seed[1]:
          if seed[0] >=line[1] and seed[0] <line[1]+line[2]:
            seed[0]+=line[0]-line[1]
            seed[1]+=1
    elif len(line)==2:
      seeds=list(map(lambda a: list((a[0],step)),seeds))
      step+=1
  print(min(seeds),len(seeds))

  
def part2():
    step = 0
    matches = re.findall(r'(\d+ \d+)', lines[0])
    seed_ranges = [tuple(map(int, match.split())) for match in matches]
    mappings={}
    for line in lines[1:]:
        line = line.split()
        if len(line) == 3:
            line = list(map(int, line))
            for seed_range in seed_ranges:
                if step > seed_range[1]:
                    if seed_range[0] >= line[1] and seed_range[0] < line[1] + line[2]:
                        seed_range[0] += line[0] - line[1]
                        seed_range[1] += 1
        elif len(line) == 2:
            seed_ranges = list(map(lambda a: list((a[0], step)), seed_ranges))
            step += 1
    
    print(min(seed_ranges))



def part22():
    step = 0
    matches = re.findall(r'(\d+ \d+)', lines[0])
    seed_ranges = [list(map(int, match.split())).append(0) for match in matches]
    mappings = {}
    print(seed_ranges)
    for line in lines[1:]:
        line = line.split()
        if len(line) == 3:
            line = list(map(int, line))
            for seed_range in seed_ranges:
                start, length = seed_range
                end = start + length
                if start <= line[0] < end:
                    line[0] = start + line[0] - end
                    seed_range[1] += 1
        elif len(line) == 2:
            seed_ranges = [[start,  vv , step] for start, length in seed_ranges]
            step += 1
    
    print(min(seed_ranges))
# zad1()
# zad2()
part22()