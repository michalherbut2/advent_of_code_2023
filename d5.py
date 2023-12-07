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
  seeds, *maps = open('input').read().split('\n\n')
  seeds = [int(seed) for seed in seeds.split()[1:]]
  maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

  locations = []
  for i in range(0, len(seeds), 2):
      ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
      results = []
      for _map in maps:
          while ranges:
              start_range, end_range = ranges.pop()
              for target, start_map, r in _map:
                  end_map = start_map + r
                  offset = target - start_map
                  if end_map <= start_range or end_range <= start_map:  # no overlap
                      continue
                  if start_range < start_map:
                      ranges.append([start_range, start_map])
                      start_range = start_map
                  if end_map < end_range:
                      ranges.append([end_map, end_range])
                      end_range = end_map
                  results.append([start_range + offset, end_range + offset])
                  break
              else:
                  results.append([start_range, end_range])
          ranges = results
          results = []
      locations += ranges
  print(min(loc[0] for loc in locations))
  
# zad1()
# zad2()
part22()