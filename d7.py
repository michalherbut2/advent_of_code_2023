import collections
import re

# f = open('in/t2')
f = open('in/i7')
lines = f.read().splitlines()
f.close()

def hand_type(hand):
  a = sorted([hand.count(h) for h in set(hand)])
  c = sorted(collections.Counter(hand).values())
  t = [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5,]].index(a)
  return t
  
def convert_hand(line):
  hand,bid=line
  return hand_type(hand), ['23456789TJQKA'.index(card) for card in hand],bid

def part1():
  hands=[(hand, int(bid)) for hand, bid in (l.split() for l in lines)]
  ordered_hands = sorted(map(convert_hand,hands))
  total=0
  for i,(*trash,bid) in enumerate(ordered_hands):
    total+=(i+1)*bid

  print(total)

def key_sort(line):
  hand,bid=line
  max_type=0
  for c in "23456789TQKA":
    new_type=hand_type(hand.replace("J",c))
    if new_type>max_type:
      max_type=new_type
  tab=max_type, *['J23456789TQKA'.index(card) for card in hand],bid
  return tab

def part2():
  hands=[(hand, int(bid)) for hand, bid in (l.split() for l in lines)]
  # ordered_hands = sorted(hands, key=key_sort)
  ordered_hands = sorted(map(key_sort,hands))
  total=0
  for i,(*trash,bid) in enumerate(ordered_hands):
    total+=(i+1)*bid
  print(total)

part1()
part2()