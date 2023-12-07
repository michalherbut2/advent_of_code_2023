import re

# f = open('in/t')
f = open('in/i6')
lines = f.read().splitlines()
f.close()

def part1():
  time, distance = lines
  time = list(map(int, time.split()[1:]))
  distance = list(map(int, distance.split()[1:]))
  stats=list(zip(time,distance))
  print(stats)
  record=1
  for _time, _distance in stats:
    ways=0
    for t in range(2,_time):
      speed = t
      d=speed*(_time-t)
      if d>_distance:
        ways+=1
    record*=ways
  print(record)
def part2():
  time, distance = lines
  time = int("".join(time.split()[1:]))
  distance = int("".join(distance.split()[1:]))
  print(time,distance)
  record=1
  ways=0
  for t in range(2,time):
    d=t*(time-t)
    if d>distance:
      ways+=1
  record*=ways
  print(record)

part1()
part2()
