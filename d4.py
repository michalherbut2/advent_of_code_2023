import re

f = open('in/i4', 'r')
lines = f.read().splitlines()
f.close()

def zad1():
  sum = 0
  for line in lines:
    line = re.sub("Card [0-9]*: ","",line)
    line=line.split(" | ")
    winNums=set(line[0].strip().split())
    myNums=set(line[1].strip().split())
    points=0
    myWinNum=len(myNums&winNums)
    if myWinNum>0:
        points=2**(myWinNum-1)
    sum+=points
  print(sum)

def zad2():
  sum = 0
  scratchcards=[1]*len(lines)
  for i,line in enumerate(lines):
    line = re.sub("Card [0-9]*: ","",line)
    line=line.split(" | ")
    winNums=set(line[0].split())
    myNums=set(line[1].split())
    
    myWinNum=len(myNums&winNums)
    for j in range(i,i+myWinNum):
        scratchcards[j+1]+=scratchcards[i]
    sum+=scratchcards[i]
  print(sum)

# zad1()
zad2()