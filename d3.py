import re

f = open('in/i3', 'r')
lines = f.read().splitlines()
f.close()

def find_symbol(i,j):
  tabWidth=len(lines[0])
  tabHeight=len(lines)
  for x in range(-1,2):
    for y in range(-1,2):
      newX=j+x
      newY=i+y
      if newX>-1 and newX<tabWidth and newY>-1 and newY<tabHeight:
        if not lines[i+y][j+x].isdecimal() and lines[i+y][j+x] != '.':
          return True
  return False

def find_asterisk(i,j):
  tabWidth=len(lines[0])
  tabHeight=len(lines)
  for x in range(-1,2):
    for y in range(-1,2):
      newX=j+x
      newY=i+y
      if newX>-1 and newX<tabWidth and newY>-1 and newY<tabHeight:
        # print(newX,newY,tabWidth,tabHeight)
        if not lines[i+y][j+x].isdecimal() and lines[i+y][j+x] != '.':
          if lines[newY][newX] == "*":
            return True,True,newY,newX
          return True,False
  return False,False

def zad1():
  suma = 0
  newNum=""
  adcjent=False
  for i,line in enumerate(lines):
    for j,znak in enumerate(line):
      if znak.isdecimal():
        newNum+=znak
        adcjent=adcjent if adcjent else find_symbol(i,j)
      else:
        if adcjent:
          suma+=int(newNum)
        newNum=""
        adcjent=False
  print(suma)

def zad2():
  suma = 0
  newNum=""
  adjacent=False
  asterisk=[]
  used={}
  for i,line in enumerate(lines):
    for j,znak in enumerate(line):
      if znak.isdecimal():
        newNum+=znak
        if not adjacent:
          res=find_asterisk(i,j)
          adjacent=res[0]
          if res[1]:
            asterisk.append(res[2])
            asterisk.append(res[3])
      else:
        if adjacent:
          if len(asterisk):
            address=f"{asterisk[0]},{asterisk[1]}"
            xd=used.get(address)
            if xd:
              used[address].append(int(newNum))
            else:
              used[address]=[int(newNum)]
            if len(used[address])==2:
              suma+=used[address][0]*used[address][1]
        newNum=""
        adjacent=False
        asterisk=[]
  print(suma)

zad1()
zad2()
