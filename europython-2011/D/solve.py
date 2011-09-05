#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Sun 04 Sep 2011 05:18:54 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys
import string

f = sys.stdin


cases = int(f.readline())

def followErs(day,monkList):
  spoken=set()
  spoken = spoken | set([day])
  before=len(spoken)
  while True:
    testLst=[]
    for i in range(len(monkList)):
      if monkList[i] in spoken:
        testLst.append(i+1)
    spoken = spoken | set(testLst)
    if before==len(spoken):
      break
    else:
      before=len(spoken)
  return before


for i in range(cases):
  monks = int(f.readline())
  monkList=map(int,f.readline().split())
  print "Case #"+str(i+1)+":"
  for day in range(monks):
    print followErs(day+1,monkList)
