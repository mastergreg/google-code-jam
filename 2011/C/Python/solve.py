#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 16-09-2011
#
#* Last Modified : Wed 21 Sep 2011 03:13:37 AM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/


import sys



def hasT(cards):
  for (c , s , t) in cards:
    if t>0:
      return True
  return False

def playT(cards):
  for i in range(len(cards)):
    #print i
    (c , s , t) = cards[i]
    if t>0:
      return cards.pop(i)

def hasC(cards):
  for (c , s , t) in cards:
    if c>0:
      return True
  return False

def playC(cards):
  maxC = 0
  maxI = 0
  for i in range(len(cards)):
    (c , s , t) = cards[i]
    if c>maxC:
      maxI = i
      maxC = c
  return cards.pop(maxI)

def lift(c , hand_l , deck_l):
  if c < len(deck_l):  
    hand_l.extend(deck_l[:c])
    del deck_l[:c]
  else:
    hand_l.extend(deck_l)
    del deck_l[:]
    #print hand_l , deck_l
def playS(cards):
  maxS = 0
  maxI = 0
  if (len(cards)==0):
    return (0,0,0)
  else:
    for i in range(len(cards)):
      (c , s , t) = cards[i]
      if s>maxS:
        maxI = i
        maxS = s
    return cards.pop(maxI)




def playBoth(score , rounds , hang , hand_list , deck_list):
  hl1 = list(hand_list)
  dl1 = list(deck_list)
  
  (c1 , s1 , t1) = playC(hl1)
  lift(c1 , hl1 , dl1)
  hand1 = len(hl1)
  rounds1 = rounds + t1 - 1
  score1 = score+s1
  score1 = play(score1 , rounds1 , hand1 , hl1 , dl1)
  
  hl2 = list(hand_list)
  dl2 = list(deck_list)

  (c2 , s2 , t2) = playS(hl2)
  lift(c2 , hl2 , dl2)
  hand2 = len(hl2)
  rounds2 = rounds + t2 - 1
  score2 = score+s2
  score2 = play(score2 , rounds2 , hand2 , hl2 , dl2)

  ans = max([score1 , score2])
  return ans 


def play(score , rounds , hand , hand_list , deck_list):
  if ( rounds>0 and hand>0):
    my_hand_list = list(hand_list)
    my_deck_list = list(deck_list)
    if hasT(my_hand_list):
      #print my_hand_list , my_deck_list
      (c , s , t) = playT(my_hand_list)
      lift(c , my_hand_list , my_deck_list)
      hand = len(my_hand_list)
      rounds += t -1
      score += s
      #print "Hand:" , my_hand_list , "Deck:" , my_deck_list
      return play(score , rounds , hand , my_hand_list , my_deck_list)
    else:
      if rounds > hand:
        if hasC(my_hand_list):
          (c , s , t) = playC(my_hand_list)
          lift(c , my_hand_list , my_deck_list)
          hand = len(my_hand_list)
          rounds += t - 1
          score += s
          return play(score , rounds , hand , my_hand_list , my_deck_list)
        else:
          (c , s , t) = playS(my_hand_list)
          lift(c , my_hand_list , my_deck_list)
          hand = len(my_hand_list)
          rounds += t - 1
          score += s
          return play(score , rounds , hand , my_hand_list , my_deck_list)
      else:
        if hasC(my_hand_list):
          return playBoth(score , rounds , hand , my_hand_list , my_deck_list)
        else:
          (c , s , t) = playS(my_hand_list)
          lift(c , my_hand_list , my_deck_list)
          hand = len(my_hand_list)
          rounds += t - 1
          score += s
          return play(score , rounds , hand , my_hand_list , my_deck_list)
  else:
    return score


def fancy_print(ls):
  print "\n#\tC\t#\tS\t#\tT\t#\n"
  print len(ls)
  for (c , s , t) in ls:
    print  "#\t" , c ,  "\t#\t" ,  s ,  "\t#\t" , t  , "\t#"


def main():
  f = sys.stdin
  cases = int(f.readline())



  for i in range(cases):
    cardsAthand = int(f.readline())
    card_at_hand_list=[]
    for j in range(cardsAthand):
      card_at_hand_list.append(tuple(map (int ,  f.readline().split())))
    cardsIndeck = int(f.readline())
    card_in_deck_list=[]
    for j in range(cardsIndeck):
      card_in_deck_list.append(tuple(map (int ,  f.readline().split())))
    rounds_left = 1
    score = 0
    #fancy_print ( card_at_hand_list)
    #fancy_print ( card_in_deck_list)
    score = play(score , rounds_left , cardsAthand , card_at_hand_list , card_in_deck_list)
    #print score

    answer = str(score)
    print "Case #"+str(i+1)+": "+answer

if __name__=="__main__":
  main()
