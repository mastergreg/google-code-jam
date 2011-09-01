#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Thu 01 Sep 2011 10:28:10 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/
import sys

f = sys.stdin


cases = int(f.readline())



for i in range(cases):
  cash = int(f.readline())
  choices = int(f.readline())
  choice_list = f.readline().split()
  initial = list(choice_list)
  for c in choice_list:
    test = str(cash-int(c))
    initial.pop(0)
    try:
      initial.index(test)
      b = choice_list.index(c)+1
      a = initial.index(test)+b+1
      #if a < b:
      #  answer = str(a)+' '+str(b)
      #else:
      answer = str(b)+' '+str(a)
      break
    except ValueError:
      continue
  print "Case #"+str(i+1)+": "+answer
