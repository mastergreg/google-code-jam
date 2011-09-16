#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 16-09-2011
#
#* Last Modified : Fri 16 Sep 2011 04:23:19 AM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/


import sys



def playMaxTurns(cards):
  maxI = 0
  maxT = 0
  for i in range(len(cards)):
    (c,s,t) = cards[i]
    if t > maxT:
      maxT = t
      maxI = i
  return maxI
def playMaxCards(cards):
  maxI = 0
  maxC = 0
  for i in range(len(cards)):
    (c,s,t) = cards[i]
    if c > maxC:
      maxC = c
      maxI = i
  return maxI
def playMaxScore(cards):
  maxI = 0
  maxS = 0
  for i in range(len(cards)):
    (c,s,t) = cards[i]
    if s > maxS:
      maxS = s
      maxI = i
  return maxI

def playGetAll(rounds,hand,deck,handList,deckList):
  if rounds > 1:


def pick_card(rds,cAh,cId,cAhL,cIdL):
  if cAh == 0:
    return 0
  if cId == 0:
    return playMaxTurns(cAhL)
  else:
    return playGetAll(rds,cAh,cId,cAhL,cIdL)



f = sys.stdin
cases = int(f.readline())



for i in range(cases):
  cardsAthand = int(f.readline())
  card_at_hand_list=[]
  for j in range(cardsAthand):
    card_at_hand_list.append(tuple(f.readline().split()))
  cardsIndeck = int(f.readline())
  card_in_deck_list=[]
  for j in range(cardsIndeck):
    card_in_deck_list.append(tuple(f.readline().split()))
  rounds_left = 1
  score = 0
  while rounds_left>0 and cardsAthand > 0:
    card_number = pick_card(rounds_left,cardsAthand,cardsIndeck,card_at_hand_list,card_in_deck_list)
    print card_at_hand_list[card_number]
    print card_in_deck_list


  answer = ""
  print "Case #"+str(i+1)+": "+answer
