import re

f = open('in/i2', 'r')
instrukcje = f.read().splitlines()
f.close()

def text_to_num(text):
  nums=["one","two","three","four","five","six","seven","eight","nine"]
  for index, num in enumerate(nums):
    text = re.sub(num,num[0]+str(index+1)+num[-1],text)
  return text
def test():
  text="eightwothree"
  text=text_to_num(text)
  x = re.sub("[a-z]","", text)
  print(x,x[0],x[-1])
# test()

def zad1():
  suma = 0
  for i in instrukcje:
    red=0
    green=0
    blue=0
    i=i.split(": ")
    index = i.pop(0).split(" ")[1]
    add=True
    # print(i)
    # print(i[0].split("; "))
    for config in i[0].split("; "):
      
      for cube in config.split(", "):
        cube=cube.split()
        # print(cube)
        if cube[1] == "red":
          if int(cube[0]) < 13:
            red += int(cube[0])
          else: 
            add=False

        elif cube[1] == "green":
          if int(cube[0]) < 14:
            green += int(cube[0])
          else: 
            add=False

        elif cube[1] == "blue":
          if int(cube[0]) < 15:
            blue += int(cube[0])
          else: 
            add=False

    print(red,green,blue)
    # if red<13 and green<14 and blue<15:
    if add:
      suma+=int(index)
  
  print(suma)

def zad2():
  suma = 0
  for i in instrukcje:
    red=0
    green=0
    blue=0
    i=i.split(": ")
    index = i.pop(0).split(" ")[1]
    
    # print(i)
    # print(i[0].split("; "))
    for config in i[0].split("; "):
      
      for cube in config.split(", "):
        cube=cube.split()
        # print(cube)
        if cube[1] == "red" :
            red = max(int(cube[0]),red)

        elif cube[1] == "green" :
            green = max(int(cube[0]),green)

        elif cube[1] == "blue" :
            blue = max(int(cube[0]),blue)

    # print(red,green,blue)
    # if red<13 and green<14 and blue<15:
  
    suma+=red*green*blue
  
  print(suma)

# zad1()
zad2()
