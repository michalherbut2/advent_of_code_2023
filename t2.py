import re

# f = open('in/t2')
f = open('in/i7')
lines = f.read().splitlines()
f.close()

def hand_type(hand):
  # return set([(h,hand.count(h)) for h in hand])
  a= [hand.count(h) for h in set(hand)]
  # print(a)
  if a.count(1)==5:
    # return 0
    return 0
  elif a.count(2)==1:
    return 1
  elif a.count(2)==2:
    return 2
  elif 3 in a:
    return 3
  elif 4 in a:
    return 4
  elif 5 in a:
    return 5
  
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

def order_hands(hands):
    # return sorted(hands, key=lambda hand: (hand_type(hand.split()[0]), [int(card)-2 if card.isdigit() else 8 + 'TJQKA'.index(card) for card in hand.split()[0]]))
    return sorted(hands, key=lambda hand: (hand_type(hand.split()[0]), [int(card)-2 if card.isdigit() else 8 + 'TJQKA'.index(card) for card in hand.split()[0]]))
def hand_type2(hand):
    L = [hand.count(_) for _ in hand]
    L.sort(reverse=True)
    return L[0] * 10 + L[1]
def score_hand(hand):
        base = str(hand_type2(hand))
        cards = '23456789TJQKA'
        s = ''.join(f'{cards.index(_):02d}' for _ in hand)
        print
        return base + s

# print(hand_type(lines[0].split()[0]))
def part1():
  # lines.sort(hand_type)
  # ordered_hands = order_hands(lines)
  # print(ordered_hands)
  hands=[line.split() for line in lines]
  hands=[(hand, int(bid)) for hand, bid in hands]
  ahands = [(score_hand(hand), bid) for hand, bid in hands]
  ahands.sort(key=lambda a:a[0])
  
  total=0
  for i,e in enumerate(ahands):
 
    total+=(i+1)*int(e[1])
    print(i, e)
  print(total)
  # hands = [(score_hand(hand), bid) for hand, bid in hands]
  # hands.sort()
  # # print(hands)
  # tot = 0
  # for i, tup in enumerate(hands):
  #     _, bid = tup
  #     tot += (i+1) * bid
  # print(tot)
  # time, distance = lines
  # time = list(map(int, time.split()[1:]))
  # distance = list(map(int, distance.split()[1:]))
  # stats=list(zip(time,distance))
  # print(stats)
  # record=1
  # for _time, _distance in stats:
  #   ways=0
  #   for t in range(2,_time):
  #     speed = t
  #     d=speed*(_time-t)
  #     if d>_distance:
  #       ways+=1
  #   record*=ways
  # print(record)

def part2():
  pass

part1()
# part2()
