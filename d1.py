import re

f = open('in/i1.txt', 'r')
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
test()

def zad1():
  suma = 0
  for i in instrukcje:
    if suma <100:
      print(i)
    i=text_to_num(i)
    if suma <100:
      print(i)
    x = re.sub("[a-z]","", i)
    # print(x)
    suma += 10 * int(x[0]) + int(x[-1])
  print(suma)

def zad2():
  pass

zad1()
# zad2()
