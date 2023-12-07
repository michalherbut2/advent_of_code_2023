import re

# f = open('in/t2')
f = open('in/i7')
lines = f.read().splitlines()
f.close()

def hand_type(hand):
  # return set([(h,hand.count(h)) for h in hand])
  a= [hand.count(h) for h in set(hand)]
  # print(a)
  if 5 in a:
    return 6
  elif 4 in a:
    return 5
  elif 3 in a and 2 in a:
    # print(hand)
    return 4
  elif 3 in a:
    return 3
  elif a.count(2)==2:
    return 2
  elif a.count(2)==1:
    return 1
  elif a.count(1)==5:
    return 0
  
def card_label(card):
  match (card):
    case ('A'):
      return 12
    case ('K'):
      return 11
    case ('Q'):
      return 10
    case ('J'):
      return 9
    case ('T'):
      return 8
    case ('9'):
      return 7
    case ('8'):
      return 6
    case ('7'):
      return 5
    case ('6'):
      return 4
    case ('5'):
      return 3
    case ('4'):
      return 2
    case ('3'):
      return 1
    case ('2'):
      return 0
      
      # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
def convert_hand(hand):
  card_values=["23456789TJQKA".index(h) for h in hand]
  # hand_value=
  pass

def order_hands(lines):
    return sorted(lines, key=lambda line: (hand_type(line[0]), *[int(card) if card.isdigit() else 10 + 'TJQKA'.index(card) for card in line[0]]))
    # return sorted(hands, key=lambda hand: (hand_type(hand.split()[0]), *[int(card)-2 if card.isdigit() else 8 + 'TJQKA'.index(card) for card in hand.split()[0]]))
    # hands=[(convert_hand(hand), int(bid)) for hand, bid in (l.split() for l in lines)]
    # return sorted(hands)


# print(hand_type(lines[0].split()[0]))
def part1():
  # lines.sort(hand_type)
  hands=[(hand, int(bid)) for hand, bid in (l.split() for l in lines)]
  ordered_hands = order_hands(hands)
  # print(ordered_hands)
  total=0
  for i,e in enumerate(ordered_hands):
 
    total+=(i+1)*int(e[1])
    # print(i, e)
  print(total)

def key_sort(line):
  hand,bid=line
  max_type=0
  for c in "23456789TQKA":
    new_type=hand_type(hand.replace("J",c))
    if new_type>max_type:
      max_type=new_type
  tab=(max_type, *['J23456789TQKA'.index(card) for card in hand]) 
  return tab

def order_hands2(lines):
    return sorted(lines, key=key_sort)
   

def part2():
  hands=[(hand, int(bid)) for hand, bid in (l.split() for l in lines)]
  print(hands[:3])
  ordered_hands = order_hands2(hands)
  # print(ordered_hands)
  total=0
  for i,e in enumerate(ordered_hands):
 
    total+=(i+1)*int(e[1])
    # print(i, e)
  print(total)

part1()
part2()
